# calculator
this is the first lab given to us
## How to use the calculator
to use the cli version of the calculator make sure you the all the neccessary requirements the run the main.py with a subcommand under the operators like divide withe the numbers 4 and 5 in the example below

```bash
uv run main.py divide 4 5
```
## How to run the code
check the instructions from [how to run file](./setup.md)
## Assignments

| Person | Task | Branch Name | Notes |
|--------|------|------------|-------|
| Asher | `add()` & `subtract()` | `feature/asher-add-subtract` | Implement basic functions |
| Billy | `multiply()` & `divide()` | `feature/billy-mul-div` | Handle division by zero |
| Cha | `modulus()` | `feature/cha-modulus` | Handle division by zero |
| @Jedaiah | `get_number_input()` basic | `feature/jedaiah-get-input` | Input prompt & loop |
| @Kabaso | `get_number_input()` error handling | `feature/kabaso-get-input-errors` | try/except & type conversion |
| @Kalaba | `update_history()` | `feature/kalaba-update-history` | Format and store history |
| Lweendo | `display_history()` | `feature/lweendo-display-history` | Handle empty history |
| Christian | Test operations with valid inputs | `feature/christian-test-valid` | Unit testing |
| SAVIOUR | Test non-numeric & zero division | `feature/saviour-test-errors` | Validate error handling |
| shadrick | Verify history & operations count | `feature/shadrick-test-history` | Confirm correctness |
| Sindi | Clear history feature | `feature/sindi-clear-history` | Bonus task |
| Temwa Chitika | Memory functions (M+, M-, MR, MC) | `feature/temwa-memory` | Bonus task |
| Vanessa | Advanced operations (exponents, sqrt) | `feature/vanessa-advanced` | Bonus task |
| Anthony | Operations on previous result | `feature/anthony-prev-result` | Bonus task |
| Joseph | GUI with Tkinter | `feature/joseph-gui` | Bonus task |

---

## Git Workflow Instructions

1. Fork the repo or clone directly if added as collaborator.
2. Create your branch:
   ```bash
   git checkout -b feature/<name>-<task>
   ```
3. Commit changes regularly:
   ```bash
   git add .
   git commit -m "Implement <task description>"
   ```
4. Push branch to remote:
   ```bash and risk 
   git push origin feature/<name>-<task>
   ```
5. Open a Pull Request (PR) to merge into `main`.
6. Once approved, merge into `main`.


