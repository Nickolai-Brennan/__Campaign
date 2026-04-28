# Workflow Registry

All registered workflows in the ai-automation system.

| ID | Name | Phase | Primary Agent | Output |
|---|---|---|---|---|
| WF-00 | project-intake | ALL | project-planner-agent | project_brief, roadmap, milestones, risk_register |
| WF-01 | data-collection | ALL | data-cleanup-agent | ingested_raw_data, data_inventory, source_report |
| WF-02 | data-cleanup | ALL | data-cleanup-agent | cleaned_dataset, cleaning_report, validation_summary |
| WF-03 | data-analysis | ALL | data-analysis-agent | analysis_report, statistical_summary, key_insights |
| WF-04 | model-development | MVP, PROD | model-development-agent | model_spec, feature_definitions, evaluation_plan |
| WF-05 | dashboard-build | PROTO, MVP | stats-visualization-agent | visualization_specs, component_plan, page_layout |
| WF-06 | api-build | ALL | api-agent | openapi_spec, service_layer_design |
| WF-07 | database-build | ALL | database-agent | ddl_sql, erd_description, migration_strategy |
| WF-08 | testing-validation | MVP, PROD | testing-agent | test_plan, test_cases, qa_checklist |
| WF-09 | documentation | MVP, PROD | documentation-agent | readme, api_reference, runbook, architecture_doc |
| WF-10 | launch-review | MVP, PROD | repo-maintenance-agent | launch_checklist, changelog, repo_health_report, go_no_go |

## Execution Order (typical project)

```
WF-00 → WF-01 → WF-02 → WF-03
                              ↓
                    WF-07 ←→ WF-04
                    WF-07 → WF-06 → WF-05
                                         ↓
                                   WF-08 → WF-09 → WF-10
```

## Phase Legend
- **PROTO**: PROTOTYPE
- **MVP**: Minimum Viable Product
- **PROD**: PRODUCTION
