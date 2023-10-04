/*
Descripción breve del programa:
Este programa calcula la Longest Common Substring (LCS) de dos cadenas de texto.

Autores: Jaime Cabrera Flores y José Carlos Sánchez Gómez
Fecha de Creación/Modificación: 1/10/2023
*/

#include <iostream>
#include <string>
#include <vector>

/*
Función: lcSubstring
Propósito: Calcular el Longest Common Substring (LCS) de dos cadenas de texto.
Parámetros:
- std::string s1: Primera cadena de texto.
- std::string s2: Segunda cadena de texto.
Retorno: Substring más grande entre dos cadenas.
Complejidad: O(n*m), donde n y m son las longitudes de las cadenas s1 y s2, respectivamente.
*/
std::string lcSubstring(std::string s1, std::string s2)
{
    int n = s1.length();
    int m = s2.length();
    std::vector<std::vector<std::string>> lcs(n + 1, std::vector<std::string>(m + 1, ""));
    std::string maxString = "";

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (s1[i - 1] == s2[j - 1])
            {
                lcs[i][j] = lcs[i - 1][j - 1] + s2[j - 1];
                if (lcs[i][j].length() > maxString.length())
                {
                    maxString = lcs[i][j];
                }
            }
        }
    }
    return maxString;
}
