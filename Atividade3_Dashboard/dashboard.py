import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from io import BytesIO

# Configure page
st.set_page_config(
    page_title="Piano Dataset Dashboard",
    page_icon="🎹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# carregando dataset
@st.cache_data
def load_data():
    return pd.read_csv('./piano_dataset_with_target.csv')

df = load_data()

# Customizando CSS
st.markdown("""
    <style>
        /* Main background and text colors  */
        .main {
            background-color: #f5f5f5;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #648ee8 0%, #243447 100%);
            color: white;
        }
        
        /* Title styling */
        h1 {
            color: #1a1a1a;
            text-align: center;
            font-weight: 700;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        /* Header styling */
        h2 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-top: 30px;
            font-weight: 600;
        }
        
        h3 {
            color: #34495e;
            margin-top: 20px;
            font-weight: 500;
        }
        
        /* Card styling */
        .metric-card {
            background-color: white;
            border-left: 5px solid #3498db;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
        
        /* Text styling */
        p {
            color: #34495e;
            line-height: 1.6;
            font-size: 30px;
        }
        
        /* Widget labels */
        label {
            color: #1dd1a1 !important;
            font-weight: 700 !important;
            font-size: 30px !important;
        }
        
        /* Selectbox styling */
        .stSelectbox label {
            color: #10ac84 !important;
            font-weight: 700 !important;
            font-size: 30px !important;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
        }
        
        /* Radio button styling */
        .stRadio > label {
            color: #1dd1a1 !important;
            font-weight: 950 !important;
            font-size: 30px !important;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
        }
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
        }
        
        .stRadio > div > div > label {
            color: #1dd1a1 !important;
            font-weight: 950 !important;
            background: linear-gradient(90deg, rgba(29, 209, 161, 0.15) 0%, rgba(29, 209, 161, 0.05) 100%);
            padding: 12px 15px;
            border-radius: 8px;
            border-left: 4px solid #1dd1a1;
            display: block;
            margin: 8px 0;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            font-size: 25px !important;
            letter-spacing: 0.5px;
            text-transform: none;
        }
        
        .stRadio > div > div > label:hover {
            background: linear-gradient(90deg, rgba(29, 209, 161, 0.25) 0%, rgba(29, 209, 161, 0.15) 100%);
            border-left: 4px solid #10ac84;
            box-shadow: 0 3px 8px rgba(29, 209, 161, 0.3);
            transform: translateX(5px);
        }
        
        /* Button styling */
        .stButton > button {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: #2980b9;
            box-shadow: 0 4px 12px rgba(52, 152, 219, 0.3);
        }
        
        /* Expander styling */
        .streamlit-expanderHeader {
            background-color: #ecf0f1;
            color: #2c3e50;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #1dd1a1 0%, #10ac84 100%);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(29, 209, 161, 0.3);
        margin-bottom: 20px;
    ">
        <h2 style="color: white; margin: 0; font-size: 28px;">🎹</h2>
        <h3 style="color: white; margin: 8px 0 0 0; font-size: 18px; font-weight: 700;">Painel de Controle</h3>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    # Widget 1: Emotion selector
    selected_emotion = st.selectbox(
        "🎵 **Selecione uma emoção:**",
        df['emotion'].unique(),
        help="Escolha a emoção para filtrar os dados"
    )
    
    # Widget 2: Feature selector
    selected_feature = st.radio(
        "📊 Selecione uma Característica:",
        ['valence', 'arousal', 'tempo'],
        format_func=lambda x: {
            'valence': '😊 Valência (Positividade)',
            'arousal': '⚡ Excitação (Energia)',
            'tempo': '🎶 Tempo (BPM)'
        }.get(x, x),
        help="Escolha a característica para análise detalhada"
    )
    
    st.markdown("---")
  
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Registros", len(df))
    with col2:
        st.metric("Emoções", df['emotion'].nunique())
    with col3:
        st.metric("BPM Médio", f"{df['tempo'].mean():.0f}")

image2 = Image.open('./assets/emotion_recognition.png')
import base64
from io import BytesIO
buffered = BytesIO()
image2.save(buffered, format="PNG")
img_b64 = base64.b64encode(buffered.getvalue()).decode()
st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{img_b64}" width="1000" height="400" alt="Emotion"></div>', unsafe_allow_html=True)
st.markdown("# 🎹 Dashboard Analítico - Piano Dataset")
st.markdown("""
        - **Nome:** RICARDO FERNANDES DE ALMEIDA
        - **Turma:** 2025.2
        - **Especialização Cesar - Engenharia e Análise de DADOS**  
        - **Disciplina: Análise e Visualização de Dados**
        - **Atividade #3 - Construção de Dashboard**
""")
st.markdown("Análise interativa de insights musicais baseada em características emocionais")
st.markdown("---")

#  abas navegação
tab1, tab2, tab3, tab4 = st.tabs(["📊 Gráficos", "📋 Estatísticas", "ℹ️ Sobre", "🖼️ Imagem"])

with tab1:
    st.markdown("## Gráficos Interativos - Análise de Insights Emocionais")
    
    col1, col2 = st.columns(2)
    
    # Prepare filtered data and scale features for sizing
    filtered_df = df[df['emotion'] == selected_emotion].copy()
    
    # Scale features to positive range for marker sizing (5-25)
    df_plot = df.copy()
    for col in ['valence', 'arousal', 'tempo']:
        min_val = df_plot[col].min()
        max_val = df_plot[col].max()
        df_plot[f'{col}_scaled'] = 5 + 20 * (df_plot[col] - min_val) / (max_val - min_val)
    
    filtered_df_plot = filtered_df.copy()
    for col in ['valence', 'arousal', 'tempo']:
        min_val = df[col].min()
        max_val = df[col].max()
        filtered_df_plot[f'{col}_scaled'] = 5 + 20 * (filtered_df[col] - min_val) / (max_val - min_val)
    
    # Calculate emotion centers for annotation
    emotion_centers = df_plot.groupby('emotion')[['valence', 'arousal', 'tempo']].mean()
    
    # Pre-calculate statistics for all possible uses
    valence_mean = filtered_df_plot['valence'].mean()
    arousal_mean = filtered_df_plot['arousal'].mean()
    tempo_median = filtered_df_plot['tempo'].median()
    tempo_mean = filtered_df_plot['tempo'].mean()
    tempo_min = filtered_df_plot['tempo'].min()
    tempo_max = filtered_df_plot['tempo'].max()
    tempo_std = filtered_df_plot['tempo'].std()
    
    # Insight #1: Dispersão dinâmica baseada em selected_feature - GRÁFICO 1
    with col1:
        if selected_feature == 'valence':
            st.markdown("### Insight #1: Valência vs Tempo")
            st.markdown(f"*Análise focada em: **Valência** | Emoção: **{selected_emotion}***")
            
            fig1 = px.scatter(
                filtered_df_plot,
                x='valence',
                y='tempo',
                color='emotion',
                size='arousal_scaled',
                hover_data=['valence', 'arousal', 'tempo'],
                title=f"Valência vs Tempo ({selected_emotion})",
                labels={
                    'valence': 'Valência (Positividade)',
                    'tempo': 'Tempo (BPM)',
                    'emotion': 'Emoção'
                },
                color_discrete_map={
                    'happy': '#FFD700',
                    'angry': '#FF4444',
                    'sad': '#4169E1',
                    'relaxed': '#9370DB'
                }
            )
            
            # Add mean lines
            fig1.add_vline(x=valence_mean, line_dash="dash", line_color="#FF6B6B", 
                          annotation_text=f"Média Val: {valence_mean:.2f}", annotation_position="top left")
            fig1.add_hline(y=tempo_mean, line_dash="dash", line_color="#95E1D3", 
                          annotation_text=f"Média Tempo: {tempo_mean:.0f}", annotation_position="top right")
            
        elif selected_feature == 'arousal':
            st.markdown("### Insight #1: Excitação vs Tempo")
            st.markdown(f"*Análise focada em: **Excitação** | Emoção: **{selected_emotion}***")
            
            fig1 = px.scatter(
                filtered_df_plot,
                x='arousal',
                y='tempo',
                color='emotion',
                size='valence_scaled',
                hover_data=['valence', 'arousal', 'tempo'],
                title=f"Excitação vs Tempo ({selected_emotion})",
                labels={
                    'arousal': 'Excitação (Intensidade)',
                    'tempo': 'Tempo (BPM)',
                    'emotion': 'Emoção'
                },
                color_discrete_map={
                    'happy': '#FFD700',
                    'angry': '#FF4444',
                    'sad': '#4169E1',
                    'relaxed': '#9370DB'
                }
            )
            
            # Add mean lines
            fig1.add_vline(x=arousal_mean, line_dash="dash", line_color="#FF6B6B", 
                          annotation_text=f"Média Arousal: {arousal_mean:.2f}", annotation_position="top left")
            fig1.add_hline(y=tempo_mean, line_dash="dash", line_color="#95E1D3", 
                          annotation_text=f"Média Tempo: {tempo_mean:.0f}", annotation_position="top right")
            
        else:  # tempo
            st.markdown("### Insight #1: Tempo vs Valência × Excitação")
            st.markdown(f"*Análise focada em: **Tempo (BPM)** | Emoção: **{selected_emotion}***")
            
            fig1 = px.scatter(
                filtered_df_plot,
                x='tempo',
                y='valence',
                color='emotion',
                size='arousal_scaled',
                hover_data=['valence', 'arousal', 'tempo'],
                title=f"Tempo vs Valência ({selected_emotion})",
                labels={
                    'tempo': 'Tempo (BPM)',
                    'valence': 'Valência (Positividade)',
                    'emotion': 'Emoção'
                },
                color_discrete_map={
                    'happy': '#FFD700',
                    'angry': '#FF4444',
                    'sad': '#4169E1',
                    'relaxed': '#9370DB'
                }
            )
            
            # Add mean lines
            fig1.add_vline(x=tempo_mean, line_dash="dash", line_color="#FF6B6B", 
                          annotation_text=f"Média Tempo: {tempo_mean:.0f}", annotation_position="top left")
            fig1.add_hline(y=valence_mean, line_dash="dash", line_color="#95E1D3", 
                          annotation_text=f"Média Val: {valence_mean:.2f}", annotation_position="top right")
        
        # Add emotion centers annotations
        for emotion in emotion_centers.index:
            if selected_feature == 'valence':
                fig1.add_annotation(
                    x=emotion_centers.loc[emotion, 'valence'],
                    y=emotion_centers.loc[emotion, 'tempo'],
                    text=emotion.upper()[:3],
                    font=dict(size=12, color='white'),
                    showarrow=True,
                    arrowsize=1,
                    arrowwidth=2,
                    arrowcolor='gray'
                )
            elif selected_feature == 'arousal':
                fig1.add_annotation(
                    x=emotion_centers.loc[emotion, 'arousal'],
                    y=emotion_centers.loc[emotion, 'tempo'],
                    text=emotion.upper()[:3],
                    font=dict(size=12, color='white'),
                    showarrow=True,
                    arrowsize=1,
                    arrowwidth=2,
                    arrowcolor='gray'
                )
            else:  # tempo
                fig1.add_annotation(
                    x=emotion_centers.loc[emotion, 'tempo'],
                    y=emotion_centers.loc[emotion, 'valence'],
                    text=emotion.upper()[:3],
                    font=dict(size=12, color='white'),
                    showarrow=True,
                    arrowsize=1,
                    arrowwidth=2,
                    arrowcolor='gray'
                )
        
        fig1.update_layout(
            height=500,
            template='plotly_white',
            hovermode='closest',
            font=dict(size=11, color='#34495e'),
            title_font_size=14,
            xaxis=dict(showgrid=True, gridwidth=1, gridcolor='#ecf0f1'),
            yaxis=dict(showgrid=True, gridwidth=1, gridcolor='#ecf0f1')
        )
        
        st.plotly_chart(fig1, use_container_width=True)
    
    # Insight #2: Distribuição dinâmica baseada em selected_feature - GRÁFICO 2
    with col2:
        if selected_feature == 'valence':
            st.markdown("### Insight #2: Distribuição de Valência")
            st.markdown(f"*Andamentos e dispersão de positividade*")
            
            fig2 = px.histogram(
                filtered_df_plot,
                x='valence',
                nbins=20,
                color='emotion',
                title=f"Distribuição de Valência - {selected_emotion}",
                labels={'valence': 'Valência (Positividade)', 'count': 'Frecuência'},
                color_discrete_map={
                    'happy': '#FFD700',
                    'angry': '#FF4444',
                    'sad': '#4169E1',
                    'relaxed': '#9370DB'
                }
            )
            
            # Add annotation
            fig2.add_vline(x=valence_mean, line_dash="dash", line_color="#FF6B6B", 
                          annotation_text=f"Média: {valence_mean:.2f}", annotation_position="top")
            
        elif selected_feature == 'arousal':
            st.markdown("### Insight #2: Distribuição de Excitação")
            st.markdown(f"*Andamentos e dispersão de intensidade*")
            
            fig2 = px.histogram(
                filtered_df_plot,
                x='arousal',
                nbins=20,
                color='emotion',
                title=f"Distribuição de Excitação (Arousal) - {selected_emotion}",
                labels={'arousal': 'Excitação (Intensidade)', 'count': 'Frequência'},
                color_discrete_map={
                    'happy': '#FFD700',
                    'angry': '#FF4444',
                    'sad': '#4169E1',
                    'relaxed': '#9370DB'
                }
            )
            
            # Add annotation
            fig2.add_vline(x=arousal_mean, line_dash="dash", line_color="#FF6B6B", 
                          annotation_text=f"Média: {arousal_mean:.2f}", annotation_position="top")
            
        else:  # tempo
            st.markdown("### Insight #2: Distribuição de Tempo (BPM) por Emoção")
            st.markdown(f"*Andamentos musicais por padrão emocional*")
            
            fig2 = px.box(
                df_plot[df_plot['emotion'].isin([selected_emotion])],
                x='emotion',
                y='tempo',
                color='emotion',
                title=f"Distribuição de Tempo (BPM) - {selected_emotion}",
                labels={'tempo': 'Tempo (BPM)', 'emotion': 'Emoção'},
                color_discrete_map={
                    'happy': '#FFD700',
                    'angry': '#FF4444',
                    'sad': '#4169E1',
                    'relaxed': '#9370DB'
                }
            )
            
            # Add median line annotation
            fig2.add_hline(y=tempo_median, line_dash="dash", line_color="#FF6B6B", 
                          annotation_text=f"Mediana: {tempo_median:.0f} BPM", annotation_position="right")
        
        fig2.update_layout(
            height=500,
            template='plotly_white',
            showlegend=False,
            font=dict(size=11, color='#34495e'),
            title_font_size=14,
            xaxis=dict(showgrid=True, gridwidth=1, gridcolor='#ecf0f1'),
            yaxis=dict(showgrid=True, gridwidth=1, gridcolor='#ecf0f1')
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # Explicações em novas colunas - DINÂMICAS DE ACORDO COM SELECTED_FEATURE
    exp_col1, exp_col2 = st.columns(2)
    
    with exp_col1:
        with st.expander("📝 Explicação do Insight #1: Dispersão de Valência e Excitação"):
            if selected_feature == 'valence':
                st.markdown(f"""
                **Análise Focada em Valência (Positividade):**
                
                A valência representa o grau de positividade/negatividade da música. Nesta análise:
                
                - 😊 **Happy**: Alta valência (positiva) 
                  Músicas alegres e otimistas com valores próximos a +1
                
                - 😠 **Angry**: Baixa valência (negativa)  
                  Músicas agressivas e intensas com valores próximos a -1
                
                - 😢 **Sad**: Baixa valência (negativa)
                  Músicas melancólicas e tristes com valores próximos a -1
                
                - 😌 **Relaxed**: Alta valência (positiva)
                  Músicas positivas mas tranquilas com valores próximos a +1
                
                **Observações para {selected_emotion}:**
                - Média de Valência: **{valence_mean:.3f}**
                - Eixo X: Valência (nosso foco)
                - Eixo Y: Excitação (dimensão secundária)
                - Tamanho das bolhas: Proporcional ao Tempo (BPM)
                - A linha vertical vermelha marca a média de valência para {selected_emotion}
                - A linha horizontal azul marca a média de excitação para comparação
                """)
            elif selected_feature == 'arousal':
                st.markdown(f"""
                **Análise Focada em Excitação/Arousal (Energia):**
                
                A excitação (arousal) representa a intensidade/energia da música. Nesta análise:
                
                - 😊 **Happy**: Alto arousal (intenso)
                  Músicas energéticas e animadas com valores próximos a +1
                
                - 😠 **Angry**: Alto arousal (muito intenso)
                  Músicas agressivas e explosivas com valores máximos
                
                - 😢 **Sad**: Baixo arousal (calmo)
                  Músicas melancólicas e apáticas com valores próximos a -1
                
                - 😌 **Relaxed**: Baixo arousal (tranquilo)
                  Músicas suaves e calmantes com valores próximos a -1
                
                **Observações para {selected_emotion}:**
                - Média de Arousal: **{arousal_mean:.3f}**
                - Eixo X: Valência (dimensão secundária)
                - Eixo Y: Excitação (nosso foco)
                - Tamanho das bolhas: Proporcional ao Tempo (BPM)
                - A linha vertical vermelha marca a média de valência
                - A linha horizontal azul marca a média de arousal para {selected_emotion}
                """)
            else:  # tempo
                st.markdown(f"""
                **Análise Focada em Tempo (BPM - Batidas Por Minuto):**
                
                O tempo (BPM) representa a velocidade/andamento da música. Relaciona-se com:
                
                - 😊 **Happy**: BPMs altos (rápidos)
                  Músicas dinâmicas e animadas, tipicamente 120-160 BPM
                
                - 😠 **Angry**: BPMs muito altos (muito rápidos)
                  Músicas agressivas e frenéticas, frequentemente acima de 140 BPM
                
                - 😢 **Sad**: BPMs baixos (lentos)
                  Músicas melancólicas e lentas, tipicamente 60-100 BPM
                
                - 😌 **Relaxed**: BPMs moderados (variados)
                  Músicas relaxantes, geralmente 80-120 BPM
                
                **Observações para {selected_emotion}:**
                - Média de Tempo: **{tempo_mean:.1f} BPM**
                - Eixo X: Valência (dimensão secundária)
                - Eixo Y: Excitação (dimensão secundária)
                - Tamanho das bolhas: **Nosso foco - Proporcional ao Tempo**
                - Bolhas maiores = Andamentos mais rápidos
                - Bolhas menores = Andamentos mais lentos
                - As linhas tracejadas marcam as médias para referência contextual
                """)
    
    with exp_col2:
        with st.expander("📝 Explicação do Insight #2: Distribuição de Tempo (BPM)"):
            if selected_feature == 'valence':
                st.markdown(f"""
                **Impacto da Valência na Distribuição de Tempo:**
                
                Como a valência influencia os andamentos musicais:
                
                - **Jó **Happy** (Alta Valência): Andamentos acelerados
                  Músicas positivas tendem a ser mais rápidas (BPMs altos)
                
                - **Angry** (Baixa Valência): Andamentos muito rápidos
                  Paradoxalmente, emoções negativas intensas usam muita velocidade
                
                - **Sad** (Baixa Valência): Andamentos lentos
                  Emoções negativas calmas usam ritmos lentos
                
                - **Relaxed** (Alta Valência): Andamentos variados
                  Emoções positivas mas calmas usam velocidades moderadas
                
                **Observações para {selected_emotion}:**
                - Mediana de BPM: **{tempo_median:.0f} BPM**
                - A caixa mostra 50% dos dados (quartis)
                - A linha interna é a mediana
                - Sem outliers significa consistência
                - Diferenças entre emoções refletem sua natureza intrínseca
                """)
            elif selected_feature == 'arousal':
                st.markdown(f"""
                **Impacto da Excitação (Arousal) na Distribuição de Tempo:**
                
                Como a intensidade influencia os andamentos musicais:
                
                - **Happy** (Alto Arousal): Andamentos acelerados
                  Músicas intensas e energéticas usam BPMs altos
                
                - **Angry** (Alto Arousal): Andamentos máximos
                  Intensidade máxima = BPMs muito elevados para transmission de agressividade
                
                - **Sad** (Baixo Arousal): Andamentos lentos
                  Baixa intensidade = ritmos lentificados e apáticos
                
                - **Relaxed** (Baixo Arousal): Andamentos moderados
                  Intensidade baixa = ritmos que promovem descanso e calma
                
                **Observações para {selected_emotion}:**
                - Mediana de BPM: **{tempo_median:.0f} BPM**
                - Correlação forte: Arousal ↑ = BPM ↑
                - A distribuição revela consistência ou variabilidade
                - Emoções intensas (Happy, Angry) tendem a BPMs altos
                - Emoções calmas (Sad, Relaxed) tendem a BPMs baixos
                """)
            else:  # tempo
                st.markdown(f"""
                **Análise Detalhada da Distribuição de Tempo (BPM):**
                
                A distribuição de andamentos musicais mostra padrões consistentes:
                
                - **Caixa (Box)**: Faixa interquartil (50% dos dados centrados)
                  Mostra onde está concentrada a maioria dos andamentos
                
                - **Linha Interna**: Mediana dos BPMs
                  Valor central que divide dados em 50/50
                
                - **Barras Verticais**: Mínimo e máximo
                  Amplitude total de andamentos por emoção
                
                - **Pontos**: Outliers (valores atípicos)
                  Normalmente ausentes, indicando consistência composicional
                
                **Padrões para {selected_emotion}:**
                - Mediana: **{tempo_median:.0f} BPM**
                - Mín: **{tempo_min:.0f} BPM**
                - Máx: **{tempo_max:.0f} BPM**
                - Desvio Padrão: **{tempo_std:.1f} BPM**
                
                **Interpretação:**
                - Distribuição estreita = Consistência estilística
                - Distribuição larga = Variabilidade de andamentos
                - Outliers inexistentes = Qualidade composicional consistente
                - A linha vermelha marca a mediana específica de {selected_emotion}
                """)


with tab2:
    st.markdown("## Estatísticas Descritivas")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<h3 style='font-weight: 700; color: #34495e;'>😊 <strong>Valência</strong></h3>", unsafe_allow_html=True)
        st.metric("Média", f"{df['valence'].mean():.3f}")
        st.metric("Mediana", f"{df['valence'].median():.3f}")
        st.metric("Desvio Padrão", f"{df['valence'].std():.3f}")
    
    with col2:
        st.markdown("<h3 style='font-weight: 700; color: #34495e;'>⚡ <strong>Excitação</strong></h3>", unsafe_allow_html=True)
        st.metric("Média", f"{df['arousal'].mean():.3f}")
        st.metric("Mediana", f"{df['arousal'].median():.3f}")
        st.metric("Desvio Padrão", f"{df['arousal'].std():.3f}")
    
    with col3:
        st.markdown("<h3 style='font-weight: 700; color: #34495e;'>🎶 <strong>Tempo</strong></h3>", unsafe_allow_html=True)
        st.metric("Média", f"{df['tempo'].mean():.0f} BPM")
        st.metric("Mediana", f"{df['tempo'].median():.0f} BPM")
        st.metric("Desvio Padrão", f"{df['tempo'].std():.0f} BPM")
    
    st.markdown("---")
    st.markdown("### Estatísticas por Emoção")
    
    stats_by_emotion = df.groupby('emotion')[['valence', 'arousal', 'tempo']].agg(['mean', 'median', 'std'])
    st.dataframe(stats_by_emotion.round(3), use_container_width=True)

with tab3:
    st.markdown("## ℹ️ Sobre o Dashboard")
    st.markdown("""
        - **Nome:** RICARDO FERNANDES DE ALMEIDA
        - **Turma:** 2025.2
        - **Especialização Cesar - Engenharia e Análise de DADOS**  
        - **Disciplina: Análise e Visualização de Dados**
        - **Atividade #3 - Construção de Dashboard**
    """)
    
    st.markdown("""
    ### Objetivo
    Este dashboard foi desenvolvido como atividade prática para dominar o **Streamlit**, 
    um framework Python poderoso para criar aplicações web de dados de forma rápida e eficiente.
    
    ### Dataset: Piano Dataset
    O **piano_dataset_with_target.csv** contém características musicais extraídas de 
    composições de piano classificadas em 4 emoções principais:
    - **Happy** 😊: Música positiva e energética
    - **Angry** 😠: Música intensa e negativa
    - **Sad** 😢: Música calma e melancólica
    - **Relaxed** 😌: Música tranquila e envolvente
    
    ### Características Analisadas
    1. **Valência**: Varia de -1 (negativo) a 1 (positivo)
    2. **Arousal**: Varia de -1 (calmo) a 1 (excitado)
    3. **Tempo**: Medido em BPM (Batidas Por Minuto)
    
    ### Recursos Utilizados
    - **Streamlit**: Framework para criação da interface web
    - **Pandas**: Manipulação e análise de dados
    - **Plotly**: Visualizações interativas
    - **CSS Customizado**: Estilização profissional
    
    ### Componentes do Dashboard
    ✅ **02 Gráficos Interativos**: Scatter plot e Boxplot  
    ✅ **02 Widgets**: Selectbox de emoção e Radio button de características  
    ✅ **01 Imagem**: Logo fixa ilustrativa  
    ✅ **Estilização CSS**: Interface profissional e responsiva  
    """)

with tab4:
    st.markdown("## 🖼️ Imagem e Visualizações")
    
    # Create columns for better layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        ">
            <h2 style="color: white; margin: 0; font-size: 48px;">🎹</h2>
            <h3 style="color: white; margin: 10px 0;">Piano Dataset</h3>
            <p style="color: rgba(255,255,255,0.9); margin: 10px 0; font-size: 14px;">
                Análise Emocional de Composições Musicais
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("")
        
        try:
            image = Image.open('../assets/logo_cesar.png')
            st.image(image, caption="Logo CESAR",  width=300)
        except FileNotFoundError:
            st.markdown("""
            <div style="
                background-color: #ecf0f1;
                padding: 30px;
                border-radius: 10px;
                text-align: center;
                border: 2px dashed #95a5a6;
            ">
                <p style="color: #7f8c8d; font-size: 14px;">
                    📁 Logo não encontrado em '../assets/logo_cesar.png'
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        ">
            <h2 style="color: white; margin: 0; font-size: 48px;">📊</h2>
            <h3 style="color: white; margin: 10px 0;">Estatísticas</h3>
            <p style="color: rgba(255,255,255,0.9); margin: 10px 0; font-size: 14px;">
                Dados Abrangentes e Detalhados
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #3498db;
        ">
            <h4 style="color: #2c3e50; margin-top: 0;">📈 Cobertura do Dataset</h4>
            <ul style="color: #34495e; line-height: 1.8;">
                <li><strong>Total de Registros:</strong> """ + str(len(df)) + """</li>
                <li><strong>Emoções Classificadas:</strong> """ + str(df['emotion'].nunique()) + """</li>
                <li><strong>Valência Média:</strong> """ + f"{df['valence'].mean():.3f}" + """</li>
                <li><strong>Arousal Médio:</strong> """ + f"{df['arousal'].mean():.3f}" + """</li>
                <li><strong>Tempo Médio:</strong> """ + f"{df['tempo'].mean():.0f} BPM" + """</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""

    """, unsafe_allow_html=True)
    st.markdown("---")
    # Widget 1: Emotion selector
