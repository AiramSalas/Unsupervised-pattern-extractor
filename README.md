# Unsupervised feature extractor.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project analyses vertical profiles of atmospheric turbulence using unsupervised deep learning techniques. Hourly heatmaps are generated from turbulence measurements across altitude levels and then transformed into multi-channel tensors to serve as input for models like CNN-EfficientNetB1 in this case, but instead of classification, the CNN is used as feature extractor of useful info for clustering.

## Features
| Feature                     | Description                                                                                |
|-----------------------------|--------------------------------------------------------------------------------------------|
| 🌪 Profile Processing       | Converts turbulence profiles into hourly heatmaps.                                         |
| 🧩 Feature extractor        | Use CNN BUT, as feature extractor from the generated heatmaps                              |
| 🌈 Multi-Channel Tensors    | Includes seasonality day-of-year encoded as sine/cosine channels+greyscale heatmap channel | 
| 🧠 Deep Learning            | Uses EfficientNetB1+advprop weights to extract hourly turbulence profiles features.        |  
| 🔍 Unsupervised Clustering  | Extracts features and create clusters without labeled data.                                |

## Screenshots
Here is an example of a turbulence heatmap as graphic generated from the data, then a greyscale png to be used in a tensor channel:

![Hourly Heatmap](screenshots/heatmap.png)
![Hourly Heatmap Greyscale](screenshots/heatmap_greyscale.png)

Some graphics generated during the clusters analysis:

Mean turbulence per cluster
![Mean Turbulence per Cluster](screenshots/mean_turbulence_cluster.png)

Presence of each cluster along the year
![Proportion and Count of each cluster along the year](screenshots/proportion_count_by_cluster.png)

Seasonal dominance
![Seasonal dominance and hours of biggest presence during the day](screenshots/seasonal_dominance.png)


## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AiramSalas/Unsupervised-pattern-extractor.git
   cd Unsupervised-pattern-extractor

2. Install dependencies, just to install common libraries, each notebook has it's own imports in the first cell.
   ```bash    
   pip install -r requirements.txt

## Usage

1. Load main Dataframes for both observatories, OT - Teide and ORM - Roque

2. Use the provided notebooks to:

   - Generate hourly heatmaps from raw profile data.

   - Create multi-channel tensors.

   - Use pre-trained model for unsupervised feature extraction and explore clustering results.

*NOTE: generated heatmaps images already included in the repo, this step is the most expensive in terms of hardware performance and time-consuming, so you can play with that part or directly use the provided images.

3. Visualise results using the provided notebook.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or suggestions.

## License
****************************************************************************
*** These data are protected by the Instituto de Astrofisica de Canarias ***
***                           COPYRIGHT (C)                              ***
****************************************************************************


