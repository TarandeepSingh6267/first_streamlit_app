# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import pandas as pd

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")
st.write(
    """Pick a sweatsuit color or style:
    """
)

# Get the current credentials
uploaded_file = st.file_uploader("Choose an image file", accept_multiple_files=False, label_visibility='hidden')
if uploaded_file is not None:
  # Convert image base64 string into hex 
  bytes_data_in_hex = uploaded_file.getvalue().hex()

  # Generate new image file name
  file_name = 'img_' + str(uuid.uuid4())

  # Write image data in Snowflake table
  df = pd.DataFrame({"FILE_NAME": [file_name], "IMAGE_BYTES": [bytes_data_in_hex]})
  session.write_pandas(df, "IMAGES")
'''
my_catlog=session.table('catalog_for_website').select(col('COLOR_OR_STYLE'))

option=st.selectbox('enter',my_catlog)

# We'll build the image caption now, since we can
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

ans=session.table('catalog_for_website').filter(col('COLOR_OR_STYLE')==option)
#st.write(ans)
p_df=ans.to_pandas()
#st.write(p_df)
#df2 = session.fetchone()


#st.write(p_df['DIRECT_URL'].iloc[0])
st.image(p_df['DIRECT_URL'].iloc[0],width=400,caption=product_caption)

st.write('Price:',p_df['PRICE'].iloc[0])
st.write('Sizes Available::',p_df['SIZE_LIST'].iloc[0])
st.write(p_df['UPSELL_PRODUCT_DESC'].iloc[0])
'''
