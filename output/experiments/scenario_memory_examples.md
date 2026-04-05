# Scenario Memory Pilot Examples

This file records the inspectable context bundles used in the pilot. The same underlying graph is queried with two context construction strategies:

- `fragment-oriented`: `node_rrf`
- `scenario-oriented`: `combined_rrf`

Scores in the companion results table are author-assigned rubric judgments for this pilot, not blinded evaluation results.

## Supplier MOQ pressure under cash-flow constraints

**Query:** How should the owner respond to supplier minimum order pressure without hurting cash flow?

### Fragment-oriented context (`node_rrf`)

- `Recommendation`: Negotiate Alternative MOQ Agreements with Supplier Collaboration Strategy — Negotiate Alternative MOQ Agreements with Supplier Collaboration Strategy. Suppliers pushing higher MOQs threaten cash flow and inventory management, but leveraging split shipments and supplier co-marketing opens an oppo
- `Owner`: Gwen O'Connell — Owner Gwen O'Connell runs County Boutique in Ennis, County Clare, selling occasion wear for weddings, communions and formal events.
- `Recommendation`: Optimize Inventory Management with Minimum Order Quantity (MOQ) Adjustments — Optimize Inventory Management with Minimum Order Quantity (MOQ) Adjustments. Strategically optimizing MOQ can lower your inventory-related expenses while addressing slower-moving lines and cash flow challenges during a c
- `OwnerCompany`: OwnerCompany Gwen O'Connell — OwnerCompany Gwen O'Connell (County Boutique), women's occasion-wear retailer in Ennis, Co. Clare. Registered 2025-10-24. Recent periods: Sep–Oct 2025 revenue fell ($18.5k→$16.2k), Oct–Nov drop to $7.4k; online mix risin
- No explicit relational evidence returned in this condition.

### Scenario-oriented context (`combined_rrf`)

- `Recommendation`: Negotiate Alternative MOQ Agreements with Supplier Collaboration Strategy — Negotiate Alternative MOQ Agreements with Supplier Collaboration Strategy. Suppliers pushing higher MOQs threaten cash flow and inventory management, but leveraging split shipments and supplier co-marketing opens an oppo
- `Owner`: Gwen O'Connell — Owner Gwen O'Connell runs County Boutique in Ennis, County Clare, selling occasion wear for weddings, communions and formal events.
- `Recommendation`: Optimize Inventory Management with Minimum Order Quantity (MOQ) Adjustments — Optimize Inventory Management with Minimum Order Quantity (MOQ) Adjustments. Strategically optimizing MOQ can lower your inventory-related expenses while addressing slower-moving lines and cash flow challenges during a c
- `RELATES_TO` fact: Goal G-20251101-cash achieved securing consignment terms with two suppliers and improved cash position for OwnerCompany Gwen O'Connell. (episodes=1)
- `RELATES_TO` fact: AI Business Advisor's recommendation to use split shipment, a 60-day sales review, and automatic top-up was triggered by Gwen O'Connell's report of suppliers wanting higher minimum order quantities. (episodes=1)
- `RELATES_TO` fact: OwnerCompany Gwen O'Connell benefited from pausing Meta ads which saved €800 and helped cash position (episodes=1)
- `RELATES_TO` fact: AI Business Advisor recommends countering with split shipment, a 60-day sales review, and a smaller opening order with automatic top-up to address the suppliers' MOQ challenge (episodes=1)
- `RELATES_TO` fact: OwnerCompany Gwen O'Connell is pursuing onboarding holiday temps quickly (owner Gwen O'Connell hiring two holiday temps) (episodes=1)

### Pilot reading

- Fragment score pattern: completeness 2/5, traceability 1/5.
- Scenario score pattern: completeness 4/5, traceability 4/5.

## Weekend staffing constraint without hurting service

**Query:** How should the owner reduce weekend rota conflicts without hurting service quality?

### Fragment-oriented context (`node_rrf`)

- `Owner`: Gwen O'Connell — Owner Gwen O'Connell runs County Boutique in Ennis, County Clare, selling occasion wear for weddings, communions and formal events.
- `Recommendation`: Implement Flexible Scheduling System to Reduce Saturday Rota Gaps and Overtime Costs — Implement Flexible Scheduling System to Reduce Saturday Rota Gaps and Overtime Costs. You can immediately address high overtime costs and operational inefficiencies by introducing a flexible, tech-enabled scheduling syst
- `Recommendation`: Implement a Rotational Weekend Staffing Model to Reduce Overtime Costs — Implement a Rotational Weekend Staffing Model to Reduce Overtime Costs. Staffing gaps on Saturdays are driving up overtime costs, but a rotational weekend model can significantly reduce these expenses while ensuring cons
- `OwnerCompany`: OwnerCompany Gwen O'Connell — OwnerCompany Gwen O'Connell (County Boutique), women's occasion-wear retailer in Ennis, Co. Clare. Registered 2025-10-24. Recent periods: Sep–Oct 2025 revenue fell ($18.5k→$16.2k), Oct–Nov drop to $7.4k; online mix risin
- No explicit relational evidence returned in this condition.

### Scenario-oriented context (`combined_rrf`)

- `Owner`: Gwen O'Connell — Owner Gwen O'Connell runs County Boutique in Ennis, County Clare, selling occasion wear for weddings, communions and formal events.
- `Recommendation`: Implement Flexible Scheduling System to Reduce Saturday Rota Gaps and Overtime Costs — Implement Flexible Scheduling System to Reduce Saturday Rota Gaps and Overtime Costs. You can immediately address high overtime costs and operational inefficiencies by introducing a flexible, tech-enabled scheduling syst
- `Recommendation`: Implement a Rotational Weekend Staffing Model to Reduce Overtime Costs — Implement a Rotational Weekend Staffing Model to Reduce Overtime Costs. Staffing gaps on Saturdays are driving up overtime costs, but a rotational weekend model can significantly reduce these expenses while ensuring cons
- `RELATES_TO` fact: OwnerCompany Gwen O'Connell suffers from Frequent Saturday rota gaps (episodes=1)
- `RELATES_TO` fact: Goal G-202511-hr-50 achieved a 52% reduction in rota conflicts for OwnerCompany Gwen O'Connell. (episodes=1)
- `ABOUT` fact: Gwen O'Connell benefits from the SMS shift-swap workflow (reduced overtime and improved coverage). (episodes=2)
- `RELATES_TO` fact: Gwen O'Connell will do the monthly roll-forward (episodes=1)
- `RELATES_TO` fact: OwnerCompany Gwen O'Connell is pursuing onboarding holiday temps quickly (owner Gwen O'Connell hiring two holiday temps) (episodes=1)

### Pilot reading

- Fragment score pattern: completeness 2/5, traceability 1/5.
- Scenario score pattern: completeness 4/5, traceability 4/5.

## Sales dip recovery under attribution uncertainty

**Query:** How should the owner respond to the October sales decline and improve November conversion?

### Fragment-oriented context (`node_rrf`)

- `Owner`: Gwen O'Connell — Owner Gwen O'Connell runs County Boutique in Ennis, County Clare, selling occasion wear for weddings, communions and formal events.
- `Goal`: G-202511-target (Increase November online conversion rate by 20% with size filter + bundles) — Goal G-202511-target: increase November online conversion rate by 20% with size filter and bundles. Status partially achieved — reached 18% in November (size filter +8%, bundles +12%). Target date 2025-11-28T09:10:00Z.
- `Entity`: User Memories for Gwen O'Connell — Owner Gwen O'Connell of County Boutique earns main revenue from occasion wear (weddings, communions, formal events) in spring and autumn; aims to grow online sales to 30% within 12 months; favors Irish/European designers
- `ResearchSummary`: Research Summary 2026-03-02 — Quick wins: Run a 10–20% off or multi-buy offer on 3–5 high-margin, everyday items with clear shelf and window signage to convert price-conscious walk-ins.; Create a simple counter display of impulse items under €10 with
- No explicit relational evidence returned in this condition.

### Scenario-oriented context (`combined_rrf`)

- `Owner`: Gwen O'Connell — Owner Gwen O'Connell runs County Boutique in Ennis, County Clare, selling occasion wear for weddings, communions and formal events.
- `Goal`: G-202511-target (Increase November online conversion rate by 20% with size filter + bundles) — Goal G-202511-target: increase November online conversion rate by 20% with size filter and bundles. Status partially achieved — reached 18% in November (size filter +8%, bundles +12%). Target date 2025-11-28T09:10:00Z.
- `Entity`: User Memories for Gwen O'Connell — Owner Gwen O'Connell of County Boutique earns main revenue from occasion wear (weddings, communions, formal events) in spring and autumn; aims to grow online sales to 30% within 12 months; favors Irish/European designers
- `RELATES_TO` fact: OwnerCompany Gwen O'Connell faces the crisis of October foot traffic and online sales down ~15%. (episodes=1)
- `ABOUT` fact: Email impacts Gwen O'Connell by driving 35% of conversions and yielding higher margin per conversion (episodes=1)
- `RELATES_TO` fact: OwnerCompany Gwen O'Connell suffers from the October drop in foot traffic and online sales (~15%). (episodes=1)
- `RELATES_TO` fact: Email marketing supports retention and higher margin per conversion for OwnerCompany Gwen O'Connell. (episodes=1)
- `ADRESSES` fact: 48-hour bundle offer on dresses and scarves addresses the October sales decline by providing a short-term promotion. (episodes=1)

### Pilot reading

- Fragment score pattern: completeness 3/5, traceability 1/5.
- Scenario score pattern: completeness 5/5, traceability 4/5.
