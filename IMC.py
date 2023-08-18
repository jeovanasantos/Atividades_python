{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP8R14l3xfx8DevcpOi5ytL",
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
        "<a href=\"https://colab.research.google.com/github/jeovanasantos/Calculo_Media/blob/main/IMC.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-pOOJ9-Jkbxn",
        "outputId": "006d4005-f071-4a9f-eae3-19276387f772"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Qual o seu nome? Ana\n",
            "Qual o seu peso? 45\n",
            "Qual a sua altura160\n",
            "Ana voce esta abaixo do peso ideal\n"
          ]
        }
      ],
      "source": [
        "# meu primeiro programa em python\n",
        "\n",
        "nome = input('Qual o seu nome? ')\n",
        "peso = float (input('Qual o seu peso? '))\n",
        "altura = float(input('Qual a sua altura '))\n",
        "imc = peso/altura ** 2\n",
        "if imc < 18.5:\n",
        "  print(f'{nome} voce esta abaixo do peso ideal')\n",
        "else:\n",
        "  if imc > 24.5:\n",
        "    print(f'{nome} voce esta acima do peso ideal ')\n",
        "  else:\n",
        "      print(f'{nome} voce esta com peso ideal ')\n"
      ]
    }
  ]
}
