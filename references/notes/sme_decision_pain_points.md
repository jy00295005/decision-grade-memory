# SME Decision Pain Points

## Executive summary

- The literature reviewed in this pass suggests that SME decision-making is difficult less because firms face a single information problem and more because several constraints interact at once: uncertainty, short-term financial pressure, limited specialized staff, incomplete or irregular information use, and relatively informal decision processes.
- The most recurring categories in the literature can be grouped into four buckets:
  - data problems
  - operational problems
  - strategic problems
  - organizational or cognitive problems
- Evidence is strongest for uncertainty, cash-flow or working-capital pressure, limited analytical and technical capacity, and owner-manager-centered decision processes.
- Evidence is moderate for fragmented systems and access-to-timely-information problems. These appear in the literature, but are less often measured directly as a unified construct.
- A defensible implication for AI support design is that SME decision support should not assume stable processes, clean integrated data, or formal analytical routines.

## Pain point taxonomy

### 1. Data problems

- Incomplete information:
  - Small-firm strategic decisions are often made under incomplete information and bounded rationality rather than under fully specified analytical conditions.
  - Salles (2006) notes that decision-support information requirements are especially difficult for SMEs, particularly for weak or unstructured tactical and strategic decisions.
  - Gibson (1992) argues that the actual use of financial information in small firms is often irregular rather than fully formalized.
- Fragmented or weakly integrated data:
  - The SME big-data review literature reports that inadequate integration into existing processes and systems leads to fragmented data sources and inefficient workflows.
  - This appears more often as a digital capability barrier than as a dedicated decision-theory variable.
- Low data literacy or weak analytical capacity:
  - Recent reviews emphasize that many SMEs lack the skills, infrastructure, and human capital needed to interpret and act on data effectively.
  - Oldemeyer, Jede, and Teuteberg (2025) and the big-data review both point to knowledge and capability constraints as recurring barriers.

### 2. Operational problems

- Cash-flow and working-capital pressure:
  - Short-term financing constraints are highly consequential for SME investment decisions.
  - Cieślik and coauthors' Small Business Economics paper shows that short-term credit constraints can force SMEs to forgo investment opportunities in order to fund working-capital needs.
  - This makes decision horizons shorter and raises the weight of liquidity-preserving choices.
- Staffing constraints:
  - The SME literature repeatedly identifies difficulty finding and retaining skilled staff as an important business pressure.
  - In the Holmes and Gupta line of work summarized by Wong, Holmes, and Schaper (2018), finding and retaining skilled staff appears among the business impact factors shaping owner decisions.
  - In adoption and transformation studies, staffing shortages also appear as limits on execution and analysis capacity.
- Limited slack and firefighting pressure:
  - SMEs typically operate with less financial, human, and organizational slack than larger firms.
  - This reduces time available for comprehensive analysis and makes operational decisions more sensitive to immediate disruptions.

### 3. Strategic problems

- Dynamic market conditions:
  - SME environments are often described as dynamic, competitive, and uncertain.
  - This increases the difficulty of comparing alternatives, assessing timing, and updating plans under shifting conditions.
- Weak competitive intelligence for unstructured decisions:
  - Salles (2006) argues that SME managers particularly struggle with information requirements for tactical and strategic decisions because these decisions are often weakly structured.
  - The problem is not only gathering information, but knowing what information is decision-relevant.
- Trade-offs across multiple objectives:
  - The optimization review for SMEs emphasizes that SMEs often face multi-objective trade-offs under uncertainty, including cost, quality, risk, timeliness, and operational constraints.
  - In practice, this means many decisions are not single-variable choices and cannot be reduced to a simple lookup or forecast.

### 4. Organizational or cognitive problems

- Owner-manager centrality:
  - In SMEs, decision authority is often concentrated in owners or a very small leadership group.
  - This reduces organizational distance between personal goals, business constraints, and final decisions.
- Informal or simple decision processes:
  - The smaller-firm decision-making literature suggests that entrepreneurs in smaller firms tend to be less comprehensive in following formal rational decision processes than professional managers in larger firms.
  - Wong, Holmes, and Schaper (2018) also reinforce that financial decisions may reflect owner goals, personal perspectives, life events, and future outlook, not only formal firm optimization.
- Bounded rationality under pressure:
  - The strategic-decision-process literature in SME contexts explicitly links incomplete information and uncertainty to heuristic decision processes.
  - This does not mean SME decisions are irrational; it means they are often satisficing, adaptive, and made with incomplete analysis.

## What is specific to SMEs vs larger firms

- SMEs typically have less managerial specialization.
  - Larger firms can distribute decision work across finance, operations, strategy, analytics, and IT functions.
  - SMEs often cannot.
- SMEs are more owner-centered.
  - Business decisions are more likely to reflect the owner-manager's goals, beliefs, and risk preferences directly.
- SMEs often rely on simpler or more informal decision routines.
  - The literature comparing smaller entrepreneurial firms with larger professionally managed firms suggests lower decision comprehensiveness in smaller firms.
- SMEs have less buffer against short-term shocks.
  - Cash-flow pressure, working-capital constraints, and staffing shortages are therefore more likely to reshape decisions quickly.
- SMEs may have weaker information infrastructure.
  - Fragmentation, irregular information use, and low integration are more consequential when there is little specialist capacity to compensate manually.

## Evidence-backed observations

1. Uncertainty is a core condition of SME decision-making rather than a peripheral complication.
   - Adomako (2022) directly studies uncertainty and decision-making in small firms.

2. Short-term finance is not a minor operational detail for SMEs; it materially shapes investment decisions.
   - The Small Business Economics evidence on working-capital constraints shows that short-term credit constraints can crowd out long-term investment.

3. SME decision processes are often less formalized and less comprehensive than those in larger professionally managed firms.
   - The Journal of Business Venturing comparison study reports lower comprehensiveness in smaller entrepreneurial firms.

4. Financial and business decisions in SMEs are often entangled with owner goals and personal circumstances.
   - Wong, Holmes, and Schaper (2018) provide qualitative evidence that owner perspectives, life events, and future outlook shape financial decisions.

5. Information requirements are particularly difficult for tactical and strategic SME decisions because these decisions are often weakly structured.
   - Salles (2006) is especially relevant here.

6. Recent SME technology reviews repeatedly identify limited skills, weak organizational readiness, poor data conditions, and integration difficulty as recurring obstacles to data-driven decision-making.
   - This appears in Oldemeyer, Jede, and Teuteberg (2025), Schwaeke et al. (2025), Hansen and Bøgh (2021), and the big-data systematic review.

## Claims needing more evidence

- TODO: stronger direct evidence that `fragmented systems` are themselves a primary decision pain point for SME owners, rather than mainly a digitalization or analytics adoption barrier.
- TODO: stronger post-2020 empirical evidence on `informal decision processes` in SMEs outside finance and entrepreneurship subfields.
- TODO: more direct evidence connecting staffing shortages to lower decision quality, not only to growth or execution difficulty.
- TODO: more empirical work on how SMEs combine external information, internal records, and owner judgment in real decision episodes.
- TODO: more evidence on how decision pain points differ by SME type, such as micro firms versus medium firms, family businesses versus professionally managed SMEs, and manufacturing versus service SMEs.

## Implications for AI support system design

- AI support for SMEs should assume incomplete, irregular, and partly informal information environments.
  - Systems should work even when records are partial and decision inputs are spread across documents, spreadsheets, messages, and tacit owner knowledge.
- AI support should be designed for low analytical slack.
  - Recommendations should reduce synthesis burden, surface missing information, and make trade-offs explicit.
- AI support should represent liquidity and operational constraints, not only abstract strategic objectives.
  - Cash-flow pressure, staffing limits, and working-capital needs are not background details; they are often decision-dominating constraints.
- AI support should help with weakly structured decisions.
  - This means identifying relevant factors, alternatives, assumptions, and unknowns rather than merely retrieving documents.
- AI support should preserve decision traceability.
  - Because SME decisions may be informal and owner-centered, systems should show what information was used, what assumptions were made, and where evidence is missing.
- TODO: the literature reviewed here does not yet prove which memory architecture best serves SME decision support. It does, however, support the design requirement that AI systems handle incomplete information, cross-source synthesis, and contextual trade-offs more explicitly than simple retrieval systems.

## Sources used in this pass

- Adomako, S. (2022). `Uncertainty and decision making in small firms`. Journal of the International Council for Small Business, 3(4). https://doi.org/10.1080/26437015.2022.2098081
- Cieślik, A., Michałek, J. J., & Mycielski, J. (2021). `Short-term financial constraints and SMEs' investment decision: evidence from the working capital channel`. Small Business Economics, 58, 1303-1321. https://doi.org/10.1007/s11187-021-00488-3
- Gibson, B. (1992). `Financial Information for Decision Making: An Alternative Small Firm Perspective`. Journal of Small Business Finance, 1(3), 221-232. https://doi.org/10.57229/2373-1761.1123
- Mitchell, R. K. (1988). `Decision making behavior in smaller entrepreneurial and larger professionally managed firms`. Journal of Business Venturing, 3(3), 223-232. https://doi.org/10.1016/0883-9026(88)90016-X
- Oldemeyer, L., Jede, A., & Teuteberg, F. (2025). `Investigation of artificial intelligence in SMEs: a systematic review of the state of the art and the main implementation challenges`. Management Review Quarterly, 75, 1185-1227. https://doi.org/10.1007/s11301-024-00405-4
- Salles, M. (2006). `Decision making in SMEs and information requirements for competitive intelligence`. Production Planning & Control, 17(3), 229-237. https://doi.org/10.1080/09537280500285367
- Schwaeke, J., Peters, A., Kanbach, D. K., Kraus, S., & Jones, P. (2025). `The new normal: The status quo of AI adoption in SMEs`. Journal of Small Business Management, 63(3), 1297-1331. https://doi.org/10.1080/00472778.2024.2379999
- Wong, A., Holmes, S., & Schaper, M. T. (2018). `How do small business owners actually make their financial decisions? Understanding SME financial behaviour using a case-based approach`. Small Enterprise Research, 25(1), 36-51. https://doi.org/10.1080/13215906.2018.1428909
- Hansen, E. B., & Bøgh, S. (2021). `Artificial intelligence and internet of things in small and medium-sized enterprises: A survey`. Journal of Manufacturing Systems, 58, 362-372. https://doi.org/10.1016/j.jmsy.2020.08.009
- Molina-Abril, G., Calvet, L., Juan, A. A., & Riera, D. (2025). `Strategic Decision-Making in SMEs: A Review of Heuristics and Machine Learning for Multi-Objective Optimization`. Computation, 13(7), 173. https://doi.org/10.3390/computation13070173
- Kgakatsi, M., Galeboe, O. P., Molelekwa, K. K., & Thango, B. A. (2024). `The Impact of Big Data on SME Performance: A Systematic Review`. Businesses, 4(4), 632-695. https://doi.org/10.3390/businesses4040038
