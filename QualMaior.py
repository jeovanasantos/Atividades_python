{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPqZ20MdQaPtv/zxaNBP9Q9",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/jeovanasantos/Calculo_Media/blob/main/QualMaior.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t0fmT5ebrrHU",
        "outputId": "26911a93-131e-45b8-e71f-74a400b2943d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero? 5\n",
            "Digite um numero? 4\n",
            "Digite um numero? 2\n",
            "O maior numero entre 5, 4 e 2 é 5\n"
          ]
        }
      ],
      "source": [
        "\n",
        "# Qual o maior numero\n",
        "num1 = int (input('Digite um numero? '))\n",
        "num2 = int (input('Digite um numero? '))\n",
        "num3 = int (input('Digite um numero? '))\n",
        "\n",
        "if (num1 > num2) and (num1 > num3):\n",
        "  maior = num1\n",
        "elif (num2 > num1) and (num2 > num3):\n",
        "  maior = num2\n",
        "elif (num3 > num1) and (num3 > num2):\n",
        "  maior = num3\n",
        "else:\n",
        "    print(\"Todos os valores sao iguais!\")\n",
        "print(f\"O maior numero entre {num1}, {num2} e {num3} é {maior}\")\n"
      ]
    }
  ]
}
