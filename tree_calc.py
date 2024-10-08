import dataframe_helper as dh

def calc_trees(combined_cities_df, final_tree_info_df, predicted_df, input_year, input_value):

    combined_cities_new_df = combined_cities_df.drop(columns=['Region', 'Population', 'Waste And Sewage', 'Machinery', 'Electricity And District Heating', 'Other Heating', 'Agriculture', 'Transportation', 'Industry'])
    final_tree_info_new_df = final_tree_info_df.drop(columns=['Species', 'Type', 'Description', 'Average Height', 'Habitat', 'Light', 'Soil', 'Water'])

    combined_cities_new_df['City With Special Characters'] = combined_cities_new_df['City'].apply(dh.reverse_special_chars_finish)
    filtered_cities_data = combined_cities_new_df[combined_cities_new_df['Year'] >= 2022][['City With Special Characters','Total Emissions']]
    filtered_cities_data = filtered_cities_data[filtered_cities_data['City With Special Characters'].str.contains(input_value, case=False)]
    #total_2022 = filtered_cities_data['Total Emissions'].iloc[0]

    input_value = dh.replace_special_chars(input_value)
    input = input_value.capitalize()
    emissions = predicted_df[input]

    year_totals = {
        '2022': emissions[10],
        '2023': emissions[11],
        '2024': emissions[12],
        '2025': emissions[13]  
    }

    if input_year in year_totals:
        year_total = year_totals[input_year]


    def calc_year(total):
        print(total)
    
        LARCH_CONSUMPTION = final_tree_info_new_df.loc[final_tree_info_new_df['Tree'] == 'Larch', 'Average CO2 Consumption'].iloc[0]
        larch_calc = int(total / LARCH_CONSUMPTION)

        PINE_CONSUMPTION = final_tree_info_new_df.loc[final_tree_info_new_df['Tree'] == 'Pine', 'Average CO2 Consumption'].iloc[0]
        pine_calc = int(total / PINE_CONSUMPTION)

        DOUGLAS_CONSUMPTION = final_tree_info_new_df.loc[final_tree_info_new_df['Tree'] == 'Douglas Fir', 'Average CO2 Consumption'].iloc[0]
        douglas_calc = int(total / DOUGLAS_CONSUMPTION)

        FIR_CONSUMPTION = final_tree_info_new_df.loc[final_tree_info_new_df['Tree'] == 'Fir', 'Average CO2 Consumption'].iloc[0]
        fir_calc = int(total / FIR_CONSUMPTION)

        SPRUCE_CONSUMPTION = final_tree_info_new_df.loc[final_tree_info_new_df['Tree'] == 'Spruce', 'Average CO2 Consumption'].iloc[0]
        spruce_calc = int(total / SPRUCE_CONSUMPTION)

        OAK_CONSUMPTION = final_tree_info_new_df.loc[final_tree_info_new_df['Tree'] == 'Oak', 'Average CO2 Consumption'].iloc[0]
        oak_calc = int(total / OAK_CONSUMPTION)

        BEECH_CONSUMPTION = final_tree_info_new_df.loc[final_tree_info_new_df['Tree'] == 'Beech', 'Average CO2 Consumption'].iloc[0]
        beech_calc = int(total / BEECH_CONSUMPTION)

        calcs = [larch_calc, pine_calc, douglas_calc, fir_calc, spruce_calc, oak_calc, beech_calc]

        return calcs
    
    filtered_rec_data = final_tree_info_new_df.copy()

    filtered_rec_data['Recommended Tree Amount'] = calc_year(year_total)

    return filtered_rec_data