.DEFAULT_GOAL := help
DB ?= neutron
GENERATE_DBS := neutron nova dw
ifeq ($(origin DB), file)
PROFILE_DBS := $(GENERATE_DBS)
else
PROFILE_DBS := $(DB)
endif
BENCH_ARGS ?= --dataset $(DB) --phase phase0
METADATA_ARGS ?=
ENRICHED_TOC_ARGS ?=
MODEL_ARGS ?= --model openai/gpt-6-luna --effort low

.PHONY: help agent-image proxy-image generate-profiles generate-schema-links generate-metadata generate-enriched-toc benchmark benchmark-smoke benchmark-pilot benchmark-post

help:
	@printf '%s\n' \
	  'make agent-image                 # build the beaver-agent sandbox image' \
	  'make proxy-image                 # build the egress proxy image' \
	  'make generate-profiles           # db-snooper profiles (all DBs; DB=neutron for one)' \
	  'make generate-schema-links       # schema-linker join hints' \
	  'make generate-metadata           # compact metadata summaries (agent-run; METADATA_ARGS="--max-turns 16")' \
	  'make generate-enriched-toc       # TOC + per-table descriptions (agent-run; ENRICHED_TOC_ARGS="--max-turns 20")' \
	  'make benchmark-smoke             # phase0: 1 question x all arms' \
	  'make benchmark-pilot             # 20 questions per DB, all arms' \
	  'make benchmark-post              # the 300-question headline run (100 per DB, all arms)' \
	  'make benchmark BENCH_ARGS="--dataset neutron --phase pilot"'

agent-image:
	docker build -t beaver-agent -f Dockerfile.agent .

proxy-image:
	docker build -t beaver-egress-proxy -f Dockerfile.proxy harness/egress

generate-profiles:
	for db in $(PROFILE_DBS); do uv run -m harness.generate_profiles --database "$$db"; done

generate-schema-links:
	for db in $(PROFILE_DBS); do uv run -m harness.generate_schema_links --database "$$db"; done

generate-metadata:
	for db in $(PROFILE_DBS); do uv run -m harness.generate_metadata --database "$$db" $(METADATA_ARGS); done

generate-enriched-toc:
	for db in $(PROFILE_DBS); do uv run -m harness.generate_enriched_toc --database "$$db" $(ENRICHED_TOC_ARGS); done

benchmark:
	@uv run run_experiment.py $(BENCH_ARGS)

benchmark-smoke:
	@uv run python run_experiment.py --phase phase0

benchmark-pilot:
	@uv run python run_experiment.py \
	 --phase main \
	 --samples dw=20 neutron=20 nova=20 \
	 $(MODEL_ARGS) \
	 --workers 4;

benchmark-post:
	@uv run python run_experiment.py \
	 --phase main \
	 --samples dw=100 neutron=100 nova=100 \
	 $(MODEL_ARGS) \
	 --workers 4;
