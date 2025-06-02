import requests
import streamlit as st
import base64
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
st.set_page_config(page_title="ماهي نبتتي؟", layout="wide")



hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_sidebar_style = """
    <style>
    section[data-testid="stSidebar"] {display: none !important;}
    div[data-testid="collapsedControl"] {display: none !important;}
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Marhey:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Scheherazade+New&display=swap');

    </style>
""", unsafe_allow_html=True) 

logo_path = "images/Logo.png"
with open(logo_path, "rb") as image_file:
    logo_base64 = base64.b64encode(image_file.read()).decode()

st.markdown(f"""
    <div style="text-align: right; padding: 0px 0px 0 0;">
        <img src="data:image/png+xml;base64,{logo_base64}" alt="Logo" style="height: 120px; margin-left: auto;">
    </div>
""", unsafe_allow_html=True)


# Navigation bar 
st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: center;
        align-items: center;
        position: sticky;
        top: -20px;
        gap: 40px;
        z-index: 1000;
        padding: 15px 10%;
        font-family: 'Marhey', sans-serif;
        font-size: 22px;
        direction: rtl;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .navbar a {
        text-decoration: none;
        font-weight: light;
        color: #333;
        transition: 0.3s ease;
        padding: 8px 15px;
        border-radius: 6px;
    }
    .navbar a:hover {
        color: #8b5e3c;
        background-color: rgba(139, 94, 60, 0.1);
    }
    .active-nav {
        color: #8b5e3c !important;
        border-bottom: 2px solid #8b5e3c;
    }
    </style>
    
    <div class="navbar">
        <a href="/Gharsa" target="_self" >الرئيسية</a>
        <a href="/Plants_info" target="_self">تعرف على النباتات</a>
        <a href="/what_is_the_plant" target="_self" class="active-nav">ماهي نبتتي؟</a>
        <a href="/Plant_your_plant" target="_self">ازرع نبتتك</a>
        <a href="/Check_your_plant" target="_self">افحص نبتتك</a>
        <a href="/Team_members" target="_self">الأعضاء</a>
    </div>
""", unsafe_allow_html=True)



with open("images/Background.png", "rb") as f:
    bg_bytes = f.read()
bg_base64 = base64.b64encode(bg_bytes).decode()

style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bg_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Marhey', sans-serif;
        color: #222;
    }}
    
    .custom-text {{
        font-family: 'Scheherazade New', sans-serif;
        font-size: 22px;
        text-align: center;
        margin: 30px 60px;
        line-height: 2;
        direction: rtl;
        color: #333;
        background-color: rgba(255,255,255,0.7);
        padding: 20px;
        border-radius: 15px;
    }}
    .custom-subtitle {{
        font-family: 'Marhey', sans-serif;
        font-size: 35px;
        text-align: center;
        margin-top: 50px;
        mergin-bottom: 20px;
        color: #4d0d0d;
    }}
    .custom-title {{
        font-family: 'Marhey', sans-serif;
        font-size: 100px;
        text-align: right;
        margin-top: 40px;
        direction: rtl;
        color: #4d0d0d;
    }}
    .soil-type-card {{
        font-family: 'Marhey', sans-serif;
        background-color: rgba(255,255,255,0.8);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 40px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    </style>
    """
st.markdown(style, unsafe_allow_html=True)





plant_icon_path = os.path.join("images", "identify_plant.png")
with open(plant_icon_path, "rb") as f:
    plant_icon_base64 = base64.b64encode(f.read()).decode()

st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 15px; justify-content: center; direction: rtl; ">
        <div style="font-family: 'Marhey', sans-serif; font-size: 60px; color: #4d0d0d; ">
        ماهي نبتتي؟ 
        </div>
        <img src="data:image/png;base64,{plant_icon_base64}" style="height: 100px;">
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='custom-text'>
    <div style="text-align: center; font-size: 22px; font-family: 'Marhey', sans-serif; color: #4d0d0d; font-weight: bold;">
        تعرف على نبتتك من خلال صورة فقط!
    </div>
    <div style="text-align: center; font-size: 18px; font-family: 'Scheherazade New', sans-serif; color: #333; font-weight: bold;">
        ما عليك إلا ترفع صورة واضحة لنبتتك، ونساعدك نحدد اسمها ونوعها وطريقة العناية المناسبة لها. <br>
    </div>
</div>

""", unsafe_allow_html=True)

check_icon_path = os.path.join("images", "what_is_the_plant.png")
with open(check_icon_path, "rb") as f:
    check_icon_base64 = base64.b64encode(f.read()).decode()

st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 15px; justify-content: center; direction: rtl; margin-top: 50px;">
        <div style="font-family: 'Marhey', sans-serif; font-size: 35px; color: #4d0d0d;">
            تعرف على نبتتك
        </div>
        <img src="data:image/png;base64,{check_icon_base64}" style="height: 100px;">
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='custom-text'>
لمساعدتك في التعرف على نبتتك  يمكنك اتباع الخطوات التالية:   
                   
1- ا         بإمكانك تصوير نبتتك كاملة أو جزء منها    2-التقط صورة واضحة         3- ارفع الصورة أدناه للتحليل
</div>
""", unsafe_allow_html=True)



st.markdown("""
<style>
/* نخلي محتوى summary عمودي وبالنص */
summary.st-emotion-cache-4rp1ik {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 6px !important;
}

/* تنسيق النص */
div.st-emotion-cache-wq5ihp.e1icttdg0 > p {
    font-family: 'Scheherazade New', sans-serif !important;
    font-size: 20px !important;
    color: #4d0d0d !important;
    text-align: center !important;
    margin: 0 !important;
}
/* السهم يكون بمحاذاة النص */
summary.st-emotion-cache-4rp1ik svg {
    order: 2 !important;
    margin: 0 !important;
}
</style>
""", unsafe_allow_html=True)



rejected_image_path = os.path.join( "images", "rejected_sample_what.jpg")  
with open(rejected_image_path, "rb") as f:
    rejected_image_base64 = base64.b64encode(f.read()).decode()
accepted_image_path = os.path.join( "images", "accepted_sample_what.jpg")
with open(accepted_image_path, "rb") as f:
    accepted_image_base64 = base64.b64encode(f.read()).decode()

with st.expander("إرشادات رفع الصورة", expanded=False):
    st.markdown(f"""
    <div style='
        direction: rtl;
        text-align: center;
        font-family: "Scheherazade New", sans-serif;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 15px;
        margin-top: 10px;
    '>
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 30px;'>
            <!-- ✅ الصور المقبولة -->
            <div>
                <h4 style="color: green;">✅ الصور المقبولة:</h4>
                <ul style="line-height: 2;">
                    <li>صور واضحة للنبتة أو الورقة بدون تشويش</li>
                    <li>الإضاءة طبيعية وموزعة بدون ظل</li>
                    <li>الصورة ملوّنة وعالية الدقة</li>
                </ul>
                <img src="data:image/jpeg;base64,{accepted_image_base64}" style="width: 50%; border-radius: 10px; margin-top: 10px;">
            </div>
            <div>
                <h4 style="color: crimson;">❌ الصور غير المقبولة:</h4>
                <ul style="line-height: 2;">
                    <li>صور فيها ظل يغطي جزء من النبتة</li>
                    <li>صور النباتات من بعيد أو بدون أوراق ظاهرة</li>
                    <li>صور مقصوصة أو مشوهة أو ضبابية</li>
                </ul>
                <img src="data:image/jpeg;base64,{rejected_image_base64}" style="width: 50%; border-radius: 10px; margin-top: 10px;">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)



# رفع الصورة
uploaded_file = st.file_uploader("اختر صورة للنبتة", type=["jpg", "jpeg", "png"], label_visibility="collapsed",  key="custom_uploader")
st.markdown("""
    <style>
    [data-testid="stFileUploader"] {
        display: flex;
        justify-content: center;
        font-family: 'Scheherazade New', sans-serif;
    }

    [data-testid="stFileUploader"] > div {
        max-width: 500px;
        width: 95%;
    }

    button[kind="primary"] {
        background-color: #8b5e3c !important;
        color: white !important;
        font-size: 20px !important;
        padding: 12px 26px !important;
        border-radius: 10px !important;
        font-family: 'Marhey', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

if uploaded_file:
    file_bytes = uploaded_file.getvalue()
    img_base64 = base64.b64encode(file_bytes).decode()

    st.markdown(f"""
        <div style="text-align: center;">
          <img src="data:image/jpeg;base64,{img_base64}"
            style="width: 250px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);" />
        <p style="font-family: 'Scheherazade New'; font-size: 16px;">🖼️ الصورة المرفوعة</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #8b5e3c !important;
            color: white !important;
            font-size: 22px !important;
            font-weight: bold !important;
            padding: 16px 36px !important;
            border-radius: 12px !important;
            font-family: 'Marhey', sans-serif !important;
            border-color: #FFFF !important;
            border-width: 2px !important;
            border-style: solid !important;
            display: block;
            margin: 30px auto;
        }
        </style>
    """, unsafe_allow_html=True)

    analyze_clicked = st.button("🔍 تعرف على النبتة ", key="analyze_btn")

    if analyze_clicked:
        with st.spinner("جاري التعرف..."):
            try:
                file_bytes = uploaded_file.getvalue()

                response = requests.post(
                    "https://multimedia-armed-initiatives-yorkshire.trycloudflare.com/recognize",
                    files={"file": file_bytes}
                )
                response.raise_for_status()
                data = response.json()
                class_name = data.get("class", "غير معروفة")

        
                plant_details = {
                    "mint": {
                        "name": "النعناع (Mint)",
                        "nickname": "عشبة الانتعاش",
                        "allergy": "نادراً ما يسبب حساسية، لكن قد يسبب تهيج للأطفال إذا تم لمسه بكثرة.",
                        "uses": "نبتة مفيدة تُستخدم للطعام، ويمكن زراعتها للزينة الخارجية في الشرفات أو الحدائق الصغيرة.",
                        "care": "تحتاج إلى ضوء شمس جزئي وتربة رطبة دائمًا، قصّ الأوراق يحفز النمو."
                        },
                    "fiddle_leaf": {
                        "name": "نبتة التين الورقي (Fiddle Leaf Fig)",
                        "nickname": "أيقونة النباتات المنزلية",
                        "allergy": "قد تسبب تهيج بسيط في الجلد، ويُنصح بإبعادها عن الحيوانات الأليفة.",
                        "uses": "نبتة زينة داخلية مميزة بأوراقها العريضة – توضع في الداخل أو بجانب النوافذ.",
                        "care": "تحتاج ضوء ساطع غير مباشر، وتُروى فقط عند جفاف التربة السطحية."
                        },
                    "aloe_vera": {
                        "name": "الألوفيرا (Aloe Vera)",
                        "nickname": "نبتة الشفاء",
                        "allergy": "قد تسبب تهيج جلدي لبعض الأشخاص، وسميّة خفيفة للقطط والكلاب عند أكلها.",
                        "uses": "نبتة علاجية وزينة خارجية، تُستخدم في ترطيب البشرة وعلاج الحروق.",
                        "care": "تُروى بكمية قليلة فقط بعد جفاف التربة تمامًا، وتحتاج ضوء شمس قوي."
                        },
                    "snake_plant": {
                        "name": "نبتة الثعبان (Snake Plant)",
                        "nickname": "منقية الجو",
                        "allergy": "سامة للقطط والكلاب إذا تم تناولها.",
                        "uses": "نبتة زينة داخلية تنقي الهواء، مثالية لغرف النوم.",
                        "care": "تتحمل الإضاءة المنخفضة، وتُروى مرة كل أسبوعين أو عند جفاف التربة."
                        },
                    "pothos": {
                        "name": "نبتة البوتس (Pothos)",
                        "nickname": "اللبلاب الذهبي",
                        "allergy": "قد تسبب تهيج خفيف في الفم أو الجلد عند الحيوانات أو الأطفال.",
                        "uses": "نبتة زينة داخلية سهلة العناية، تُستخدم في المكاتب والمطابخ.",
                        "care": "تتحمل الإضاءة المنخفضة، وتُروى عند جفاف التربة بشكل جزئي."
                        },
                    "Dracaena": {
                        "name": "الدراسينا (Dracaena)",
                        "nickname": "نبتة الزينة الطويلة",
                        "allergy": "سامة للقطط والكلاب، لكنها آمنة للبشر.",
                        "uses": "زينة داخلية أنيقة، تنمو عموديًا وتناسب الزوايا.",
                        "care": "تُفضل الإضاءة المتوسطة وتُروى مرة أسبوعيًا مع تجنب الغمر."
                        },
                    "Parsley": {
                        "name": "البقدونس (Parsley)",
                        "nickname": "ما له لقب شائع",
                        "allergy": "نادرًا ما يسبب حساسية، آمن عمومًا.",
                        "uses": "نبتة غذائية تُزرع في شرفة المطبخ لاستخدامها طازجة.",
                        "care": "يحتاج إلى شمس مباشرة وري منتظم، مع قص الأوراق بشكل دوري."
                        },
                    "Cilantro": {
                        "name": "الكزبرة (Cilantro)",
                        "nickname": "عطر المطبخ",
                        "allergy": "قد تسبب تهيج بسيط نادرًا.",
                        "uses": "نبتة غذائية للطبخ، تنمو بسرعة.",
                        "care": "تحتاج ضوء شمس مباشر جزئي، وتُروى عندما تجف التربة."
                        },
                    "schismatoglottis": {
                        "name": "شيزماتوجلوتس (Schismatoglottis)",
                        "nickname": "الأخضر الملكي",
                        "allergy": "سامة للحيوانات الأليفة إذا تم تناولها.",
                        "uses": "نبتة زينة داخلية.",
                        "care": "تحتاج ضوء متوسط إلى منخفض ورطوبة عالية، لا تعرضها للشمس المباشرة."
                        },
                    "Chamaedorea elegans": {
                        "name": "شاميدوريا إليغانس (Chamaedorea Elegans)",
                        "nickname": "نخلة الزينة",
                        "allergy": "آمنة تمامًا للأطفال والحيوانات.",
                        "uses": "نخلة صغيرة للزينة داخل المنزل.",
                        "care": "تحتاج إلى ضوء خافت أو متوسط، وري معتدل كلما جفّت التربة السطحية."
                        }, 
                    "Sansevieria trifasciata ‘Golden Hahnii’": {
                        "name": "سانسيفيريا الذهبية القصيرة (Golden Hahnii)",
                        "nickname": "السانسيفيريا الصغيرة",
                        "allergy": "قد تكون سامة للحيوانات الأليفة إذا تم أكلها (خصوصًا القطط والكلاب).",
                        "uses": "نبتة زينة داخلية أنيقة وصغيرة الحجم، مثالية للمكاتب والطاولات الجانبية.",
                        "care": "تتحمل الإضاءة المنخفضة، وتُروى فقط عند جفاف التربة تمامًا – لا تحب الرطوبة الزائدة."
                        }
                    }
                
                
                
                plant_info = plant_details.get(class_name, None)
                st.markdown(f"""
                            <div style="direction: rtl; text-align: center; font-family: 'Scheherazade New', sans-serif; font-size: 22px; color: #333; margin-top: 30px;">
                        <h3>🌿 الاسم الكامل:</b> {plant_info['name']}</b></h3>
                    </div>
                """, unsafe_allow_html=True)
                if plant_info:
                    st.markdown(f"""
                        <div style="
                            background-color: rgba(255, 255, 255, 0.8);
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 30px;
                            margin-bottom: 40px;
                            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                            direction: rtl;
                            font-family: 'Scheherazade New', sans-serif;
                            font-size: 20px;
                            text-align: center;
                            line-height: 2;
                            color: #333;
                        ">
                            <p><b>🏷️ اللقب:</b> {plant_info['nickname']}</p>
                            <p><b>⚠️ مسببات الحساسية:</b> {plant_info['allergy']}</p>
                            <p><b>🌸 الاستخدامات:</b> {plant_info['uses']}</p>
                            <p><b>🪴 طرق العناية:</b> {plant_info['care']}</p>
                        </div>
                    """, unsafe_allow_html=True)



                else:
                    st.warning("❕ لم نجد معلومات إضافية عن هذه النبتة حالياً.")


            except Exception as e:
                st.error("❌ لم يتم الاتصال بـ FastAPI أو حدث خطأ.")
                st.exception(e)
