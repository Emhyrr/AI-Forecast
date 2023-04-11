from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd

model_1H = load_model('Stacking')
model_24H = load_model('Stack24')

def predict(model, input_df):
    prediction_df = predict_model(estimator=model, data=input_df)
    rain_map = {1: 'Tidak Hujan', 2: 'Hujan Ringan', 3: 'Hujan Sedang', 4: 'Hujan Lebat'}
    prediction_df['prediction_label'] = prediction_df['prediction_label'].map(rain_map)
    predictions = prediction_df['prediction_label'][0]
    return predictions

def main():
    from PIL import Image
    image = Image.open('logo.png')
    image_stmkg = Image.open('stmkg.png')

    st.image(image, use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
        "How would you like to predict?",
        ("1 Hour Rainfall", "24 Hour Rainfall"))

    st.sidebar.info('Creator Contact: emirhazam24@gmail.com')
    st.sidebar.success('https://meteorologi.stmkg.ac.id')

    st.sidebar.image(image_stmkg)

    st.title("Input Parameter")

    if add_selectbox == '1 Hour Rainfall':
        CLOUD_LOW_TYPE_CL = st.selectbox('CLOUD_LOW_TYPE_CL', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], index=9)
        CLOUD_BASE_M_H = st.number_input('CLOUD_BASE_M_H', min_value=300,max_value=750, value=540, step=10)
        CLOUD_LOW_MED_AMT_OKTAS = st.selectbox('CLOUD_LOW_MED_AMT_OKTAS', [0,1,2,3,4,5,6,7,8], index=5)
        CLOUD_COVER_OKTAS_M = st.selectbox('CLOUD_COVER_OKTAS_M', [0,1,2,3,4,5,6,7,8], index=8)
        LAND_COND = st.selectbox('LAND_COND', [0,1,2,3], index=2)
        PAST_WEATHER_W1 = st.selectbox('PAST_WEATHER_W1', [0,1,2,3,4,5,6,7,8,9], index=6)
        PAST_WEATHER_W2 = st.selectbox('PAST_WEATHER_W2', [0,1,2,3,4,5,6,7,8,9], index=6)
        PRESENT_WEATHER_WW = st.selectbox('PRESENT_WEATHER_WW', [1,2,3,4,5,6,10,12,13,14,15,16,17,19,
                                                                 20,21,22,23,25,27,28,29,40,41,46,50,60,
                                                                 61,62,63,64,65,80,91,92,93,94,95,96,97])
        TEMP_DEWPOINT_C_TDTDTD = st.number_input('TEMP_DEWPOINT_C_TDTDTD', min_value=14.0, max_value=27.6, value=24.4,
                                                 step=0.1)
        TEMP_DRYBULB_C_TTTTTT = st.number_input('TEMP_DRYBULB_C_TTTTTT', min_value=21.3, max_value=35.2, value=25.9,
                                                step=0.1)
        TEMP_WETBULB_C = st.number_input('TEMP_WETBULB_C', min_value=19.9, max_value=24.8, value=23.0, step=0.1)
        VISIBILITY_VV = st.number_input('VISIBILITY_VV', min_value=1, max_value=15, value=5)
        WIND_DIR_DEG_DD = st.number_input('WIND_DIR_DEG_DD', min_value=0, max_value=360, value=280, step=10)
        WIND_SPEED_FF = st.number_input('WIND_SPEED_FF', min_value=0, max_value=36, value=5)
        RELATIVE_HUMIDITY_PC = st.number_input('RELATIVE_HUMIDITY_PC', min_value=34, max_value=100, value=91)
        PRESSURE_QFF_MB_DERIVED = st.number_input('PRESSURE_QFF_MB_DERIVED', min_value=1002.3, max_value=1018.9,
                                                  value=1012.2, step=0.1)
        PRESSURE_QFE_MB_DERIVED = st.number_input('PRESSURE_QFE_MB_DERIVED', min_value=1000.9, max_value=1015.0,
                                                  value=1012.9, step=0.1)
        output = ("")
        input_dict = {'CLOUD_LOW_TYPE_CL': CLOUD_LOW_TYPE_CL, 'CLOUD_BASE_M_H': CLOUD_BASE_M_H,
                      'CLOUD_LOW_MED_AMT_OKTAS': CLOUD_LOW_MED_AMT_OKTAS, 'CLOUD_COVER_OKTAS_M': CLOUD_COVER_OKTAS_M,
                      'LAND_COND': LAND_COND, 'PAST_WEATHER_W1': PAST_WEATHER_W1, 'PAST_WEATHER_W2': PAST_WEATHER_W2,
                      'PRESENT_WEATHER_WW': PRESENT_WEATHER_WW, 'TEMP_DEWPOINT_C_TDTDTD': TEMP_DEWPOINT_C_TDTDTD,
                      'TEMP_DRYBULB_C_TTTTTT': TEMP_DRYBULB_C_TTTTTT, 'TEMP_WETBULB_C': TEMP_WETBULB_C,
                      'VISIBILITY_VV': VISIBILITY_VV, 'WIND_DIR_DEG_DD': WIND_DIR_DEG_DD,
                      'WIND_SPEED_FF': WIND_SPEED_FF, 'RELATIVE_HUMIDITY_PC': RELATIVE_HUMIDITY_PC,
                      'PRESSURE_QFF_MB_DERIVED': PRESSURE_QFF_MB_DERIVED,
                      'PRESSURE_QFE_MB_DERIVED': PRESSURE_QFE_MB_DERIVED}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model_1H, input_df=input_df)
            output =str(output)

        st.success('Diprediksi akan {}'.format(output))
    if add_selectbox == '24 Hour Rainfall':
        CLOUD_LOW_TYPE_CL = st.selectbox('CLOUD_LOW_TYPE_CL', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], index=9)
        CLOUD_BASE_M_H = st.number_input('CLOUD_BASE_M_H', min_value=300,max_value=750, value=540, step=10)
        CLOUD_LOW_MED_AMT_OKTAS = st.selectbox('CLOUD_LOW_MED_AMT_OKTAS', [0,1,2,3,4,5,6,7,8], index=5)
        CLOUD_COVER_OKTAS_M = st.selectbox('CLOUD_COVER_OKTAS_M', [0,1,2,3,4,5,6,7,8], index=8)
        LAND_COND = st.selectbox('LAND_COND', [0,1,2,3], index=2)
        PAST_WEATHER_W1 = st.selectbox('PAST_WEATHER_W1', [0,1,2,3,4,5,6,7,8,9], index=6)
        PAST_WEATHER_W2 = st.selectbox('PAST_WEATHER_W2', [0,1,2,3,4,5,6,7,8,9], index=6)
        PRESENT_WEATHER_WW = st.selectbox('PRESENT_WEATHER_WW', [1,2,3,4,5,6,10,12,13,14,15,16,17,19,
                                                                 20,21,22,23,25,27,28,29,40,41,46,50,60,
                                                                 61,62,63,64,65,80,91,92,93,94,95,96,97])
        TEMP_DEWPOINT_C_TDTDTD = st.number_input('TEMP_DEWPOINT_C_TDTDTD', min_value=14.0, max_value=27.6, value=24.4,
                                                 step=0.1)
        TEMP_DRYBULB_C_TTTTTT = st.number_input('TEMP_DRYBULB_C_TTTTTT', min_value=21.3, max_value=35.2, value=25.9,
                                                step=0.1)
        TEMP_WETBULB_C = st.number_input('TEMP_WETBULB_C', min_value=19.9, max_value=24.8, value=23.0, step=0.1)
        VISIBILITY_VV = st.number_input('VISIBILITY_VV', min_value=1, max_value=15, value=5)
        WIND_DIR_DEG_DD = st.number_input('WIND_DIR_DEG_DD', min_value=0, max_value=360, value=280, step=10)
        WIND_SPEED_FF = st.number_input('WIND_SPEED_FF', min_value=0, max_value=36, value=5)
        RELATIVE_HUMIDITY_PC = st.number_input('RELATIVE_HUMIDITY_PC', min_value=34, max_value=100, value=91)
        PRESSURE_QFF_MB_DERIVED = st.number_input('PRESSURE_QFF_MB_DERIVED', min_value=1002.3, max_value=1018.9,
                                                  value=1012.2, step=0.1)
        PRESSURE_QFE_MB_DERIVED = st.number_input('PRESSURE_QFE_MB_DERIVED', min_value=1000.9, max_value=1015.0,
                                                  value=1012.9, step=0.1)
        output = ""
        input_dict = {'CLOUD_LOW_TYPE_CL': CLOUD_LOW_TYPE_CL, 'CLOUD_BASE_M_H': CLOUD_BASE_M_H,
                      'CLOUD_LOW_MED_AMT_OKTAS': CLOUD_LOW_MED_AMT_OKTAS, 'CLOUD_COVER_OKTAS_M': CLOUD_COVER_OKTAS_M,
                      'LAND_COND': LAND_COND, 'PAST_WEATHER_W1': PAST_WEATHER_W1, 'PAST_WEATHER_W2': PAST_WEATHER_W2,
                      'PRESENT_WEATHER_WW': PRESENT_WEATHER_WW, 'TEMP_DEWPOINT_C_TDTDTD': TEMP_DEWPOINT_C_TDTDTD,
                      'TEMP_DRYBULB_C_TTTTTT': TEMP_DRYBULB_C_TTTTTT, 'TEMP_WETBULB_C': TEMP_WETBULB_C,
                      'VISIBILITY_VV': VISIBILITY_VV, 'WIND_DIR_DEG_DD': WIND_DIR_DEG_DD,
                      'WIND_SPEED_FF': WIND_SPEED_FF, 'RELATIVE_HUMIDITY_PC': RELATIVE_HUMIDITY_PC,
                      'PRESSURE_QFF_MB_DERIVED': PRESSURE_QFF_MB_DERIVED,
                      'PRESSURE_QFE_MB_DERIVED': PRESSURE_QFE_MB_DERIVED}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model_24H, input_df=input_df)
            output =str(output)

        st.success('Diprediksi akan {}'.format(output))

if __name__ == '__main__':
    main()
