'use strict';

const celsius = parseFloat(prompt("Введите температуру в градусах Цельсия: "));
const fahrenheit = celsius * 9 / 5 + 32;
alert(`Цельсий:${celsius}, Фаренгейт:${fahrenheit.toFixed(1)}`);
