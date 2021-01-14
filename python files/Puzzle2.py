{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Puzzle02.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPaPZTd9aKXa8dxcKBPt+YP",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SafiyyahKazim/Google-COLAB/blob/master/Puzzle02.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 130
        },
        "id": "JTQz1AnE52_I",
        "outputId": "263344f8-a645-4314-b5b7-9fa4ae50e95c"
      },
      "source": [
        "def sum_para():\n",
        "  num= 1\n",
        "  if num!= int(num):\n",
        "    print('Answer is 0')\n",
        "    print(\"wrong input...BYE!\")\n",
        "    return 0;\n",
        "    range = list (range(num+1))\n",
        "    if num == 1\n",
        "    return 1;\n",
        "  else:\n",
        "    sum= 0\n",
        "    for i in range: \n",
        "        count = sum +1\n",
        "    return sum \n",
        "\n",
        "sum_para(num)\n",
        "\n"
      ],
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-32-2c7164423ea2>\"\u001b[0;36m, line \u001b[0;32m8\u001b[0m\n\u001b[0;31m    if num == 1\u001b[0m\n\u001b[0m               ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 266
        },
        "id": "VQuVqQsZ6lrk",
        "outputId": "25d2c55d-1254-4365-d1b2-72e2e097f52b"
      },
      "source": [
        "def para(number):  \n",
        "  num=1\n",
        "  sum=0\n",
        "while num < number + 1:\n",
        "  sum=sum+num\n",
        "  num = num+1\n",
        "return sum"
      ],
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-38-7c1ba8047dfe>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m   \u001b[0mnum\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m   \u001b[0msum\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mwhile\u001b[0m \u001b[0mnum\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mnumber\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m   \u001b[0msum\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0msum\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0mnum\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m   \u001b[0mnum\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnum\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'number' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5Fcoe-66APpQ"
      },
      "source": [
        "para(5)"
      ],
      "execution_count": 39,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PFfshXCsAfha"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}