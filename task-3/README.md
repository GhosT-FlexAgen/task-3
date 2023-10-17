# Maze on Python

[![CI/CD Github Actions](https://github.com/GhosT-FlexAgen/task-3/actions/workflows/pytest.yml/badge.svg)](https://github.com/GhosT-FlexAgen/task-3/actions/workflows/pytest.yml)
[![Coverage Status](https://coveralls.io/repos/github/GhosT-FlexAgen/task-3/badge.svg?branch=master)](https://coveralls.io/github/GhosT-FlexAgen/task-3?branch=master)

[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=GhosT-FlexAgen_task-3&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=GhosT-FlexAgen_task-3)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=GhosT-FlexAgen_task-3&metric=bugs)](https://sonarcloud.io/summary/new_code?id=GhosT-FlexAgen_task-3)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=GhosT-FlexAgen_task-3&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=GhosT-FlexAgen_task-3)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=GhosT-FlexAgen_task-3&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=GhosT-FlexAgen_task-3)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=GhosT-FlexAgen_task-3&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=GhosT-FlexAgen_task-3)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=GhosT-FlexAgen_task-3&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=GhosT-FlexAgen_task-3)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=GhosT-FlexAgen_task-3&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=GhosT-FlexAgen_task-3)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=GhosT-FlexAgen_task-3&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=GhosT-FlexAgen_task-3)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=GhosT-FlexAgen_task-3&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=GhosT-FlexAgen_task-3)

Генерация случайных лабиринтов производится с помощью алгоритма [Random PRIM](https://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm). Данный алгоритм подразумевает лабиринт нечётной площади (длина и  ширина лабиринта - нечетные числа). Данный алгоритм генерации гарантирует, что в сгенерированном лабиринте из левого верхнего угла всегда будет хотя бы 1 маршрут в правый нижний угол. Именно поэтому в игре эти точки выбраны статичными точками старта и финиша.

[1]: pictures/maze.png
[2]: pictures/win.png
[3]: pictures/lose.png

![][1]
Рисунок 1. Основной экран игры.</br></br>

![][2]
Рисунок 2. Экран победы. </br></br>

![][3]
Рисунок 3. Экран поражения.</br></br>
