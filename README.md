<div id="Header" align="center">
<h1>Sudoku📝</h1>
  <img src="https://github.com/GoshaGoshanidze/Sudoku/blob/main/Sudoku/images/SudokuLogo.png" width="40%">
</div>

---

<div id="Title">
  <h2>Описание:</h2>
  <p>Консольная игра-судоку, написанная на Python, в которой не требуется наличие игрока. При каждом новом запуске программы благодаря функции generation() генерируется
    новая случайная сетка судоку, пока она не будет соответствовать правилам или пока не истекут 5 секунд.</p>
  <p>Код написан в процедурном стиле и не использует объектно-ориентированное программирование.</p>
</div>

---

<div id="Image" align="center">
  <img src="https://github.com/GoshaGoshanidze/Sudoku/blob/main/Sudoku/images/SudokuPresent.png" width="60%">
</div>

---

<div id="TitleFunctions">
<h2>Основные функции:</h2>
  <li>generation() - генерирует новую случайную сетку судоку, пока она не будет соответствовать правилам, или пока не истечёт 5 секунд;</li>
  <li>validation(num, row, column, grid) - проверяет, можно ли поместить число в указанную ячейку таблицы, не нарушая правил судоку;</li>
  <li>fill(grid, row, column) - Пытается заполнить сетку судоку, начиная с заданной ячейки, следуя правилам;</li>
  <li>print_sudoku(grid) - печатает готовую сетку судоку, заменяя все незаполненные ячейки на точки.</li>
</div>
