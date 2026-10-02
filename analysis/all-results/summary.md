## Static review summary

**Evidence base:** 300 saved verdicts across three `n100` runs—100 each for DW, Neutron, and Nova. These are LLM reviews, not independently executed SQL checks; “plausible” or “correct” below reflects the review text, not verified correctness.

### Observed patterns

- **DW:** Reviews often flag grain, join, filter, and population mismatches across arms. Examples include wrong aggregation grain (`dw_4833`, `dw_3069`), scope or population issues (`dw_4506`, `dw_4746`), and join/cardinality risks (`dw_1066`, `dw_2960`). Raw and profile answers are frequently criticized, but there are also plausible answers in both arms (`dw_5144`, `dw_5171`); no-links is not consistently better or worse (`dw_4917`, `dw_4344`).
- **Neutron:** Reviews often find profile/raw answers plausible, while raising concerns about gold joins and window scope. Examples include plausible answers with gold-side concerns (`neutron_546`, `neutron_453`, `neutron_997`) and repeated warnings about join fanout or filtering before windows (`neutron_943`, `neutron_921`, `neutron_975`). Other reviews flag answer-side scope or metric errors (`neutron_925`, `neutron_734`, `neutron_612`).
- **Nova:** Reviews describe both plausible answers and substantive errors across arms. Recurring concerns include metadata/cache joins, grouping grain, and window scope: for example, extra or questionable cache joins (`nova_104`, `nova_995`), grouping/grain mismatches (`nova_1017`, `nova_101`), and window-scope issues (`nova_1009`). Profile and raw are not uniformly separated in apparent quality; some verdicts call all arms plausible (`nova_519`, `nova_238`), while others identify errors in multiple arms (`nova_168`, `nova_36`).

### False-negative possibilities and gold/wording concerns

- Some reviews suggest **plausible answers may have been penalized** for incidental differences or uncertain semantics: ordering-only differences (`neutron_997`, `nova_562`), extra columns (`neutron_579`), and alternative but plausible interpretations (`dw_595`, `nova_115`).
- **Gold queries are frequently questioned**, especially for joins that may duplicate or omit rows, incorrect or underspecified window scope, and filters that may not match the request. Examples: `dw_3793`, `neutron_450`, `nova_440`.
- Wording ambiguity is explicitly noted around population and scope, including “at least” versus strict thresholds (`neutron_104`, `nova_165`), tenant or shared-network scope (`neutron_945`, `neutron_989`), and ranking/grouping definitions (`nova_115`, `dw_116`).

### Unresolved uncertainty

The verdicts do not establish whether any query returns the correct results: there is no independent execution evidence here. Many judgments are explicitly tentative (“plausible,” “may,” “uncertain”), and no agent traces are provided to explain why an answer took a particular approach. Counts of specific error types are therefore not reported.
