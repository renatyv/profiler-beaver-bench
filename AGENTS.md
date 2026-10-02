Agentic text-to-SQL experiment: does a pre-generated [db-snooper](https://github.com/renatyv/db-snooper)
profile of the target DB improve a coding agent's **execution accuracy** on
[BEAVER](https://huggingface.co/datasets/BeaverBench/beaver), vs. raw DB access?

Project is managed by `uv`.

The BEAVER databases are loaded to MySQL running in docker on localhost port 3307, user and password in the .env file. Use `--skip-ssl`.
