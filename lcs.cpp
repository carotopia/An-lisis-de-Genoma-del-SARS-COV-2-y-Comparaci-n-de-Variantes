
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
