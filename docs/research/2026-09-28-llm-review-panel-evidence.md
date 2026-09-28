# LLM Review Panel: What the Literature Says (2023–2026)

*Research note for `rl-review-panel`. Compiled 2026-09-28 by a research agent with web access; every source was opened, not cited from memory. Three citations were then re-checked by hand against their pages: Wu et al. 2026 and Jin & Chen 2026 matched; Ziegenbein et al. 2026 matched only in the paper body, and its entry below is corrected to say so. Written after the panel's first live test (a review of the "Available now: Reventure Labs Content OS" post), which returned 22 findings, 9 of them P0. The design implications are proposals, not yet applied to the skill.*

**Method.** I opened every source cited here (arXiv abstract or HTML pages). The Science Advances version of Doshi & Hauser returned HTTP 403, so I cite its arXiv preprint. Numbers are as reported on the pages I opened. **Domain tags:** [prose] = writing or NLG, [code], [math/QA] = reasoning benchmarks, [general] = mixed chat. Evidence from code, math and QA transfers only weakly to prose.

---

## 1. Severity calibration and over-flagging

**What the evidence shows**
- **LLM critics produce false positives, including made-up problems.** McAleese et al. (2024) found that model critiques beat human reviews on real code bugs, preferred 63% of the time. The critics also produced "hallucinated bugs that could mislead humans," and human+AI teams had fewer false positives than AI alone. [code] https://arxiv.org/abs/2407.00215
- **Asking for more detail makes over-flagging worse.** Jin & Chen (2026) found that LLMs often judge correct code as defective. "More detailed prompt design, particularly with those requiring explanations and proposed corrections, leads to higher misjudgment rates." Their fix is a verification filter that checks each suggested fix. [code] https://arxiv.org/abs/2603.00539
- **False alarms are the main barrier in deployed review tools.** Lu et al. (2025, ICML) list false-alarm rate as a core challenge and add a dedicated filtering stage. [code] https://arxiv.org/abs/2505.17928
- **Conflicting result.** In a different setting, LLM *judges* are too lenient: true-positive rate 96% but true-negative rate under 25%. Majority vote across 14 LLMs did not fix this, while a "minority-veto" rule helped (Jain et al., 2025). [code-feedback grading] https://arxiv.org/abs/2510.11822 The direction of the bias seems to depend on framing. A model asked to *find problems* over-finds them. A model asked whether something is *acceptable* tends to say yes.
- **Scores are skewed and prompt-sensitive.** Stureborg et al. (2024) report skewed rating distributions, anchoring across attributes, and low inter-sample agreement. [prose: summarization] https://arxiv.org/abs/2405.01724
- **Critics can be generic and lopsided.** In Liang et al. (2023), GPT-4 paper reviews overlapped with human reviews about as much as humans overlap with each other (30.85% for Nature, 39.23% for ICLR). But GPT-4 over-emphasized some aspects (e.g., "add experiments") and was 10.69× less likely than humans to comment on novelty. [prose: scientific] https://arxiv.org/abs/2310.01783
- **Mitigations with evidence:**
  - Rubrics plus reference answers: Prometheus reached Pearson 0.897 with humans. https://arxiv.org/abs/2310.08491
  - Breaking judgments into yes/no checklists raised judge–human agreement from 46.4% to 52.2% (Cook et al., 2024, TICK). [general] https://arxiv.org/abs/2410.03608
  - Rating each dimension separately instead of one overall score (Wu & Aji, 2023). https://arxiv.org/abs/2307.03025

**Strength:** moderate for code, weak-to-moderate for prose. I found no study that directly measures severity inflation (P0 vs P2) in prose critique, and none that tests an explicit "no issues found" option.

## 2. Several independent critics vs. one

**What the evidence shows**
- **A diverse panel of judges can beat one large judge.** A panel of smaller models from different families outperformed a single GPT-4 judge on 6 datasets, at more than 7× lower cost, with less intra-model bias (Verga et al., 2024, "PoLL"). [QA / general] https://arxiv.org/abs/2404.18796
- **Debate between critics is not reliably better than independent voting.**
  - Smit et al. (2023): multi-agent debate "do[es] not reliably outperform" self-consistency or ensembling, and is sensitive to hyperparameters. [QA/math] https://arxiv.org/abs/2311.17371
  - Choi et al. (2025, NeurIPS spotlight): "Majority Voting alone accounts for most of the performance gains" attributed to debate, across 7 NLP benchmarks. https://arxiv.org/abs/2508.17536
  - Wynn et al. (2025): during debate, models switch from correct to incorrect answers through sycophancy and conformity, and accuracy can fall over time. [reasoning] https://arxiv.org/abs/2509.05396
- **Evidence in favour of debate or role decomposition:**
  - ChatEval (Chan et al., 2023) reports gains over single-agent evaluation on open-ended NLG. https://arxiv.org/abs/2308.07201
  - Liang et al. (2024) show that single-model self-reflection gets stuck on its first answer ("Degeneration-of-Thought"), which debate relieves. [translation/arithmetic] https://arxiv.org/abs/2305.19118
  - Specialized agents improved long-form stories, as judged by experts (Huot et al., 2025, "Agents' Room"). This concerns generation, not critique. [prose: fiction] https://arxiv.org/abs/2410.02603
- **Agreement between models is weaker evidence than it looks.** Across more than 350 LLMs, errors are substantially correlated: models agree 60% of the time when both are wrong. Larger, more accurate models are highly correlated even across providers (Kim et al., 2025, ICML). [QA benchmarks + LLM-as-judge] https://arxiv.org/abs/2506.07962

**Strength:** moderate, and almost all from QA and reasoning tasks. Independent sampling plus aggregation is better supported than interactive debate. No study I found tests independent lenses (one critic per dimension) against one critic of equal budget on prose.

## 3. Using a different model family as judge

**What the evidence shows**
- **Judges favour their own output.** Panickssery et al. (2024) found LLMs rate their own outputs higher than humans do. Self-recognition ability correlates linearly with the size of the bias. [prose: summarization] https://arxiv.org/abs/2404.13076
- **The deeper cause is familiarity, not authorship.** Wataoka et al. (2024) found that LLMs give higher ratings to lower-perplexity text "regardless of whether the outputs were self-generated." Stureborg et al. (2024) also found a familiarity (low-perplexity) bias. https://arxiv.org/abs/2410.21819 ; https://arxiv.org/abs/2405.01724 This means switching to another model family reduces self-preference but not the general preference for fluent, predictable text.
- **Other judge biases:**
  - Position, verbosity and self-enhancement biases (Zheng et al., 2023). https://arxiv.org/abs/2306.05685
  - Length bias: controlling for it raised AlpacaEval's correlation with Chatbot Arena from 0.94 to 0.98 (Dubois et al., 2024). https://arxiv.org/abs/2404.04475
  - Judges rate answers with factual errors above answers that are short or ungrammatical (Wu & Aji, 2023). https://arxiv.org/abs/2307.03025
  - Ye et al. (2024) catalogue 12 judge biases. https://arxiv.org/abs/2410.02736
- **Mixed model families help, within limits.** They reduce intra-model bias (Verga et al., 2024), but Kim et al. (2025) show cross-provider errors remain correlated.

**Strength:** strong and replicated for the existence of the biases, partly on prose. Moderate for cross-family mitigation.

## 4. Iterative refinement

**What the evidence shows**
- **Self-Refine gains shrink with each round** (Madaan et al., 2023; max 4 iterations). For example, constrained generation went 29.0 → 40.3 → 46.7 → 49.7. Quality "may not always monotonically increase" in multi-aspect tasks, where one aspect improves while another declines. [mixed, including prose tasks] https://arxiv.org/abs/2303.17651
- **Specific feedback matters most.** In the same paper, task-specific feedback beat generic feedback (sentiment reversal 43.2 vs 31.2). Of the failures, 61% came from feedback suggesting an inappropriate fix and 33% from mislocating the error.
- **Self-critique without an outside check is unreliable.**
  - Huang et al. (2024, ICLR): without external feedback, LLMs struggle to self-correct and sometimes get worse. [math/QA] https://arxiv.org/abs/2310.01798
  - Kamoi et al. (2024, TACL survey): no work shows successful self-correction from prompted self-feedback, except in tasks unusually suited to it. Reliable external feedback is key. https://arxiv.org/abs/2406.01297
  - Xu et al. (2024): self-bias is present in 6 LLMs and grows over self-refinement rounds, including translation and constrained text generation. Larger models and accurate external feedback mitigate it. [partly prose] https://arxiv.org/abs/2402.11436
- **Many rounds converge on a generic text.**
  - Ziegenbein et al. (2026), "Teaching LLMs Human-Like Editing of Inappropriate Argumentation via Reinforcement Learning": applying the authors' own RL-trained editor for 11 rounds reduced fluency (Δ −0.304) and argument-level similarity (Δ −0.243); "iterative application drives the text toward a generic state of appropriateness at the cost of preserving the argument's original intent and linguistic fluency" (§6.1). The abstract reports the method's single-pass gains; the drift result is in the body and applies to that one editor, not LLM revision in general. [prose: argumentation] https://arxiv.org/abs/2604.12770
  - Wu et al. (2026): over 10 recursive refinements of 50 abstracts, "most edits occur within the first few iterations," then text settles into a model-preferred fixed point. They propose stopping when edit size stops changing. [prose: scientific abstracts] https://arxiv.org/abs/2607.22653

**Strength:** moderate. Consistent across domains that gains come early, that external or specific feedback beats self-feedback, and that long loops drift. The two drift papers are recent preprints.

## 5. Homogenization and author voice

**What the evidence shows**
- **Instruction-tuned models reduce content diversity.** Writing with InstructGPT, but not base GPT-3, significantly reduced diversity. The loss came from the model's contributions; the users' own text was unaffected (Padmakumar & He, 2024, ICLR). [prose: essays] https://arxiv.org/abs/2309.05196
- **Stories get better individually but more alike collectively.** With GenAI ideas, stories were rated better written and more enjoyable, but were more similar to each other. The effect was largest for less experienced writers (Doshi & Hauser, 2023/2024). [prose: fiction; arXiv version opened, journal page 403] https://arxiv.org/abs/2312.00506
- **AI suggestions pull writers toward a dominant style.** In an experiment with 118 participants, AI suggestions led Indian participants to adopt Western writing styles (Agarwal et al., 2025, CHI). [prose] https://arxiv.org/abs/2409.11360
- **Model text shares the same habits across families.** Professional writers' edits of 1,057 AI paragraphs produced a 7-category taxonomy of idiosyncrasies (clichés, unnecessary exposition, and others). GPT-4o, Claude-3.5 and Llama-3.1 shared them ("common limitations across model families"). Automated editing helped, but expert edits were still preferred (Chakrabarty et al., 2025, CHI). [prose] https://arxiv.org/abs/2409.14509
- **LLMs imitate informal personal style poorly.** Across 400+ authors, LLMs imitated formal writing such as news and emails adequately, but "struggle with nuanced, informal writing in blogs and forums" from a few examples (Wang et al., 2025, EMNLP Findings). [prose] https://arxiv.org/abs/2509.14543
- **Synthesis:** Sourati et al. (2025) review evidence that LLMs "reflect and reinforce dominant styles." This is a review, not new data. https://arxiv.org/abs/2508.01491
- **Link to Q3:** judges' preference for low-perplexity text (Wataoka; Stureborg) is a plausible way critic-driven revision flattens voice. The Keeper may share that bias.

**Strength:** moderate and consistent, mostly from AI *generation or suggestion*. I found no study isolating diagnosis-only critique (no rewrites) and its effect on voice.

---

## Design implications

1. **Treat 9 P0s out of 22 findings as a likely calibration problem.** Critics told to find problems over-find them (McAleese; Jin & Chen). Changes:
   - Define P0/P1/P2 with concrete anchors and a worked example of each (Prometheus; Stureborg).
   - Require a quoted passage plus a stated reader consequence for every finding.
   - Allow "no significant issues" as an explicit output.
   - Consider a cap or a justification threshold for P0.
2. **Add a verification pass before revision.** A separate call checks whether each P0/P1 finding is real at the quoted passage, analogous to the verification filter in Jin & Chen and the false-alarm filter in Lu et al. Human+AI review cut false positives (McAleese).
3. **Keep lenses blind and independent, and do not add debate between them.** Aggregation explains most debate gains, and debate causes conformity (Choi; Wynn; Smit). The current design is confirmed.
4. **Discount cross-lens agreement when the lenses share a model.** Errors correlate across models (Kim 2025), and shared training habits are documented in prose (Chakrabarty). Options:
   - Weight agreement more when it spans model families (Verga).
   - Consider a minority-veto rule for "is this fixed?" checks (Jain).
5. **Run lenses and the Keeper on a different model family from the drafter.** This addresses self-preference (Panickssery; Xu). It will not remove the familiarity or length bias (Wataoka; Dubois), so the Keeper should not reward smoother or longer text as such.
6. **Limit revisions to 1–2 rounds, with a stopping rule.** Gains come early, and many rounds drift toward generic prose (Madaan; Ziegenbein; Wu 2026). Stop when findings stop falling in severity or when edits get small.
7. **Keep feedback specific and diagnostic.** Specific feedback beats generic (Madaan), and multi-dimensional ratings beat one overall score (Wu & Aji). This confirms the lens-per-dimension design.
8. **Strengthen the voice check with measurement, not only Keeper judgment.** Homogenization is documented (Padmakumar; Doshi; Agarwal), and LLMs imitate informal voice poorly (Wang). Two options:
   - Compare the revised draft against a corpus of the author's own writing with stylometric features, or with an authorship-verification style check.
   - Have the author, not the LLM, accept or reject each change.
   - Also look for the 7 idiosyncrasy categories (Chakrabarty) *introduced* by revision.

## Open questions for our own blind A/B test

- Does a panel of 4–5 prose lenses beat a single critic with the same token budget on final quality as judged by humans? No prose study answers this.
- Does anchored severity (plus an "abstain" option) lower the P0 rate without missing real problems? That needs human-labelled ground truth for our drafts.
- Is cross-lens agreement actually predictive of findings humans rate as important, given correlated errors?
- Does diagnosis-only feedback preserve voice better than rewrite-style feedback? No direct evidence found.
- How many revision rounds are optimal for each genre (email vs. case study vs. deck)?
- Does a cross-family Keeper still favour smoother, more generic revisions? This needs human raters blind to condition.
