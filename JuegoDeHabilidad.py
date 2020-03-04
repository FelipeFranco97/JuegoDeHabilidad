{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "JuegoDeHabilidad.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPs3EvV1PIkWQQPoNPbe55t",
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
        "<a href=\"https://colab.research.google.com/github/FelipeFranco97/JuegoDeHabilidad/blob/master/JuegoDeHabilidad.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C7F78BVMwhlN",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import statistics\n",
        "%matplotlib inline\n",
        "\n",
        "lista_resultados = ['5', '15', '30', '50', '100']\n",
        "\n",
        "resultado = np.random.choice(lista_resultados, size=(10), p=[0.35, 0.25, 0.20, 0.15, 0.05])\n",
        "\n",
        "media=pd.to_numeric(resultado, errors='coerce').mean()\n",
        "\n",
        "varianza = pd.to_numeric(resultado, errors='coerce').var()\n",
        "\n",
        "print(resultado)\n",
        "print(media)\n",
        "print(varianza)\n",
        "plt.hist(resultado)\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IF4ijMGPwprm",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}