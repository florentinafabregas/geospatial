import pandas as pd
import os

def process_movements(input_path, output_path):
    df = pd.read_csv(input_path)
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])

    df = df.sort_values(by=['licencePlate', 'start_time']).reset_index(drop=True)

    # Shift within each licencePlate
    df['next_start_time'] = df.groupby('licencePlate')['start_time'].shift(-1)
    df['end_lat'] = df.groupby('licencePlate')['lat'].shift(-1)
    df['end_lon'] = df.groupby('licencePlate')['lon'].shift(-1)
    df['end_zip'] = df.groupby('licencePlate')['zipCode'].shift(-1)
    df['end_area_name'] = df.groupby('licencePlate')['area_name'].shift(-1)

    movement_df = df.copy()

    # Movement 
    movement_df['start_move_time'] = movement_df['end_time']
    movement_df['end_move_time'] = movement_df['next_start_time']
    movement_df['move_duration'] = (
        movement_df['end_move_time'] - movement_df['start_move_time']
    )

    movement_df['start_area_name'] = movement_df['area_name']

    movement_df = movement_df.dropna(subset=['end_move_time']).copy()
    movement_df = movement_df.rename(columns={
        'zipCode': 'start_zip'
    })


    movement_df['start_lat'] = movement_df['lat']
    movement_df['start_lon'] = movement_df['lon']

    movement_df = movement_df[[
        'licencePlate',
        'car_type',
        'vehicleTypeId',

        'start_move_time',
        'end_move_time',

        'start_lat', 'start_lon',
        'end_lat', 'end_lon',

        'start_zip', 'end_zip',
        'start_area_name', 'end_area_name',

        'move_duration'
    ]]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save to CSV
    movement_df.to_csv(output_path, index=False)


if __name__ == "__main__":
    input_file = "../data/raw/transformed_output.csv"
    output_file = "../data/raw/movement.csv"

    process_movements(input_file, output_file)