# Urban Mobility in Greater Copenhagen: Car-sharing Demand and Flows

### Authors

- Florentina Fabregas Alippi (flfa@itu.dk)
- Jobayer Hossain (hoss@itu.dk)

### Project Structure

```text
geospatial/
├── data/
│   ├── movement.csv
│   ├── transformed_output.csv
│   └── population_municipalities.csv
│
├── notebooks/                     # analysis notebooks
│   ├── time-series-EDA
│   ├── choropleth_popular_municipalities_area
│   ├── Demand_Supply_gap_analysis
│   ├── hop_clustering_tendency
│   ├── DBSCAN_clustering
│   └── flows
│
├── artifacts/                    # output visualizations/maps
│
├── src/
│   └── movement_dataset.py       # creates movement dataset from available parking
│
├── .gitignore
└── README.md
