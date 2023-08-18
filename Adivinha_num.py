{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN/jJEChTzCMhOyzKQouyni",
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
        "<a href=\"https://colab.research.google.com/github/jeovanasantos/Atividades_python/blob/main/Adivinha_num.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k47pGT7L_RPv",
        "outputId": "e7c3f32e-229f-435e-caf6-3218d22b45a2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Chute um numero: 7\n",
            "errou, tente um numero menor\n",
            "Chute um numero: 2\n",
            "errou, tente um numero maior\n",
            "Chute um numero: 6\n",
            "errou, tente um numero menor\n",
            "Chute um numero: 4\n",
            "errou, tente um numero menor\n",
            "Chute um numero: 3\n",
            "acertou com 5 tentativas\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "\n",
        "num = random.randint(1,9)\n",
        "jog = 0\n",
        "while True:\n",
        "  player = int(input(\"Chute um numero: \"))\n",
        "  jog += 1\n",
        "  if player < num:\n",
        "    print('errou, tente um numero maior')\n",
        "  elif player > num:\n",
        "    print('errou, tente um numero menor')\n",
        "  else:\n",
        "    print(f'acertou com {jog} tentativas')\n",
        "    break\n"
      ]
    }
  ]
}
