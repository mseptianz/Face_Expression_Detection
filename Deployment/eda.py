import matplotlib.pyplot as plt
import streamlit as st

# Mendefinisikan train & test per kategori
def run():
    train_data = {'Ahegao': 500, 'Angry': 500, 'Happy': 500, 'Neutral': 500, 'Sad': 500, 'Surprise': 500}
    test_data = {'Ahegao': 200, 'Angry': 200, 'Happy': 200, 'Neutral': 200, 'Sad': 200, 'Surprise': 200}

    # Streamlit App
    def pie_chart(data, title):
        #st title 
            
            fig, ax = plt.subplots()
            ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
            ax.set_title(title)
            st.pyplot(fig)

    st.title ('Exploratory Data Analysis - Expression Detection ')
    # Horizontal line 
    st.write('---')

            # input banner 
    st.image('https://idseducation.com/wp-content/uploads/2022/11/Thumbnail-Program-Kemang-12730_In-Your-Face.jpg')

    st.title("Data Distribution \nTrain & Test")

    # Pie chart untuk dataset training
    pie_chart(train_data, "Training Dataset Image Counts")
   
    # Pie chart untuk dataset testing
    pie_chart(test_data, "Testing Dataset Image Counts")
    # Insight 
    st.write('''Dari Visualisasi diatas diketahui :
                    \n - Kedua dataset memiliki distribusi kelas yang sangat seimbang. Masing-masing kelas (ahegao, angry, happy, neutral, sad, surprise) memiliki proporsi yang hampir sama. 
                    \n- Keseimbangan ini menunjukkan bahwa data training dan testing memiliki representasi yang baik untuk setiap kelas emosi. Ini penting karena model akan dilatih dengan data yang seimbang dan diharapkan dapat menggeneralisasi dengan baik ke data baru yang juga memiliki distribusi kelas yang serupa.''')


if __name__ == '__main__':
        run()