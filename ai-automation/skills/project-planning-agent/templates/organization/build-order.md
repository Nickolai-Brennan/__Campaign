# Build Order

## Build Sequence

| Step | Task | Depends On | Priority |
|------|------|-----------|---------|
| 1 | Project setup (repo, environments) | — | P0 |
| 2 | Documentation setup | Project setup | P0 |
| 3 | Design system / style guide | Docs | P1 |
| 4 | Database schema | Research, PRD | P0 |
| 5 | API design | Database schema | P0 |
| 6 | Backend core | API design | P0 |
| 7 | Auth / access control | Backend core | P0 |
| 8 | Frontend scaffold | Design system | P1 |
| 9 | MVP feature build | Backend + Frontend | P0 |
| 10 | Integration and testing | All above | P0 |
| 11 | Launch prep | Testing complete | P0 |

## Do First

_(The minimum needed before any code is written)_

1.
2.
3.

## Do Later

_(Important but not blocking MVP)_

- 
- 

## Do Not Build Yet

_(Explicitly deferred — do not start without user approval)_

- 
- 
- 
