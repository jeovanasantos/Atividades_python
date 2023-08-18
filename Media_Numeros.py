{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyORT7l6h/htgV+0v41xc7zv",
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
        "<a href=\"https://colab.research.google.com/github/jeovanasantos/Atividades_python/blob/main/Media_Numeros.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UQCmOM_qdpuT",
        "outputId": "569d0cfe-f8bd-4345-81cb-553a6d255ef3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero (ou digite 0 para parar): 0\n",
            "Nenhum numero foi inserido\n"
          ]
        }
      ],
      "source": [
        "total = 0\n",
        "cont = 0\n",
        "mais_numeros = True\n",
        "\n",
        "while mais_numeros:\n",
        "  numero = float(input(\"Digite um numero (ou digite 0 para parar): \"))\n",
        "  if numero == 0:\n",
        "    mais_numeros = False\n",
        "  else:\n",
        "      total += numero\n",
        "      cont += 1\n",
        "if cont == 0:\n",
        "  print(\"Nenhum numero foi inserido\")\n",
        "else:\n",
        "  media = total / cont\n",
        "  print (f\"A media dos numeros é {media: .2f}\")"
      ]
    }
  ]
}
