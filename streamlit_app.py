# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import pandas as pd
# importing necessary libraries
import img2pdf
from PIL import Image
import os
# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")
st.write(
    """Pick a sweatsuit color or style:
    """
)

# Get the current credentials
uploaded_file = st.file_uploader("Choose an image file", accept_multiple_files=False, label_visibility='hidden')
if uploaded_file is not None:
    
        # Python3 program to convert image to pdf
    # using img2pdf library
     
    
     
    # storing image path
    img_path = "C:/Users/Admin/Desktop/GfG_images/do_nawab.png"
     
    # storing pdf path
    pdf_path = "C:/Users/Admin/Desktop/GfG_images/file.pdf"
     
    # opening image
    image = Image.open(img_path)
     
    # converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image.filename)
     
    # opening or creating pdf file
    file = open(pdf_path, "wb")
     
    # writing pdf files with chunks
    file.write(pdf_bytes)
     
    # closing image file
    image.close()
     
    # closing pdf file
    file.close()
     
    # output
    print("Successfully made pdf file")
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
