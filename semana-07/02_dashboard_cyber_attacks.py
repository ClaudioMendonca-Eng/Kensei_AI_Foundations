from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ── Configuração da página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Cyber Attacks Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS moderno ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* fundo geral */
    [data-testid="stAppViewContainer"] { background: #0d1117; }
    [data-testid="stSidebar"]          { background: #161b22; border-right: 1px solid #30363d; }
    section.main > div                 { padding-top: 1rem; }

    /* título principal */
    .dash-title {
        font-size: 2.6rem !important; font-weight: 800 !important; color: #e6edf3 !important;
        letter-spacing: .5px; margin-bottom: .2rem; line-height: 1.2 !important;
    }
    .dash-sub {
        font-size: 1rem !important; color: #8b949e !important; margin-bottom: 1.5rem;
    }

    /* cards KPI */
    .kpi-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        text-align: center;
    }
    .kpi-label { font-size: .78rem; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; }
    .kpi-value { font-size: 1.9rem; font-weight: 700; color: #e6edf3; margin: .3rem 0; }
    .kpi-delta-red   { font-size: .8rem; color: #f85149; }
    .kpi-delta-green { font-size: .8rem; color: #3fb950; }

    /* abas */
    [data-testid="stTabs"] button {
        color: #8b949e !important; font-weight: 500;
    }
    [data-testid="stTabs"] button[aria-selected="true"] {
        color: #58a6ff !important; border-bottom: 2px solid #58a6ff !important;
    }

    /* dataframe */
    [data-testid="stDataFrame"] { border: 1px solid #30363d; border-radius: 8px; }

    /* separador */
    hr { border-color: #30363d; }
    </style>
    """,
    unsafe_allow_html=True,
)

TEMPLATE = "plotly_dark"
COLOR_SEQ = px.colors.qualitative.Bold

# ── Dados ────────────────────────────────────────────────────────────────────
csv_path = Path(__file__).parent / "Global_Cybersecurity_Threats_2015-2024.csv"

if not csv_path.exists():
    st.error("Arquivo **Global_Cybersecurity_Threats_2015-2024.csv** não encontrado na pasta da semana-07.")
    st.stop()


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    return df


df_full = load_data(csv_path)

# ── Sidebar – filtros ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🔎 Filtros")

    years_all = sorted(df_full["Year"].unique())
    year_range = st.slider(
        "Período",
        min_value=int(min(years_all)),
        max_value=int(max(years_all)),
        value=(int(min(years_all)), int(max(years_all))),
    )

    attack_types = sorted(df_full["Attack Type"].unique())
    selected_attack = st.multiselect("Tipo de Ataque", attack_types, default=attack_types)

    countries = sorted(df_full["Country"].unique())
    selected_country = st.multiselect("País", countries, default=countries)

    industries = sorted(df_full["Target Industry"].unique())
    selected_industry = st.multiselect("Setor Alvo", industries, default=industries)

    st.divider()
    st.caption("Kensei AI Foundations · Semana 07")

# ── Filtro aplicado ──────────────────────────────────────────────────────────
df = df_full[
    (df_full["Year"] >= year_range[0])
    & (df_full["Year"] <= year_range[1])
    & (df_full["Attack Type"].isin(selected_attack))
    & (df_full["Country"].isin(selected_country))
    & (df_full["Target Industry"].isin(selected_industry))
].copy()

# ── Cabeçalho ────────────────────────────────────────────────────────────────
st.markdown('<p class="dash-title">🛡️ Cyber Attacks Dashboard</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="dash-sub">Ataques cibernéticos globais · 2015 – 2024 · fonte: Global Cybersecurity Threats Dataset</p>',
    unsafe_allow_html=True,
)

# ── KPIs ─────────────────────────────────────────────────────────────────────
total_incidentes    = len(df)
perda_total         = df["Financial Loss (in Million $)"].sum()
usuarios_afetados   = int(df["Number of Affected Users"].sum())
tempo_medio_res     = df["Incident Resolution Time (in Hours)"].mean()

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(
        f'<div class="kpi-card"><p class="kpi-label">Incidentes</p>'
        f'<p class="kpi-value">{total_incidentes:,}</p>'
        f'<p class="kpi-delta-red">🔴 registros filtrados</p></div>',
        unsafe_allow_html=True,
    )
with k2:
    st.markdown(
        f'<div class="kpi-card"><p class="kpi-label">Perda Financeira</p>'
        f'<p class="kpi-value">$ {perda_total:,.0f} M</p>'
        f'<p class="kpi-delta-red">💸 acumulado</p></div>',
        unsafe_allow_html=True,
    )
with k3:
    st.markdown(
        f'<div class="kpi-card"><p class="kpi-label">Usuários Afetados</p>'
        f'<p class="kpi-value">{usuarios_afetados:,}</p>'
        f'<p class="kpi-delta-red">👤 total</p></div>',
        unsafe_allow_html=True,
    )
with k4:
    st.markdown(
        f'<div class="kpi-card"><p class="kpi-label">Resolução Média</p>'
        f'<p class="kpi-value">{tempo_medio_res:.1f} h</p>'
        f'<p class="kpi-delta-green">⏱ por incidente</p></div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ── Abas ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Visão Geral", "💰 Financeiro", "🌍 Geográfico", "🗺️ Mapa Interativo", "🗂️ Dados"])

# ── Tab 1 · Visão Geral ───────────────────────────────────────────────────────
with tab1:
    c1, c2 = st.columns(2)

    with c1:
        by_type = (
            df.groupby("Attack Type", as_index=False)["Financial Loss (in Million $)"].sum()
            .sort_values("Financial Loss (in Million $)", ascending=False)
        )
        fig = px.bar(
            by_type, x="Financial Loss (in Million $)", y="Attack Type",
            orientation="h", color="Attack Type",
            color_discrete_sequence=COLOR_SEQ,
            title="Perda financeira por tipo de ataque",
            template=TEMPLATE,
        )
        fig.update_layout(showlegend=False, plot_bgcolor="#161b22", paper_bgcolor="#0d1117")
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        by_industry = (
            df.groupby("Target Industry", as_index=False)["Number of Affected Users"].sum()
            .sort_values("Number of Affected Users", ascending=False)
        )
        fig2 = px.bar(
            by_industry, x="Number of Affected Users", y="Target Industry",
            orientation="h", color="Target Industry",
            color_discrete_sequence=COLOR_SEQ,
            title="Usuários afetados por setor",
            template=TEMPLATE,
        )
        fig2.update_layout(showlegend=False, plot_bgcolor="#161b22", paper_bgcolor="#0d1117")
        st.plotly_chart(fig2, use_container_width=True)

    trend = (
        df.groupby("Year", as_index=False)["Financial Loss (in Million $)"].sum()
        .sort_values("Year")
    )
    fig3 = px.area(
        trend, x="Year", y="Financial Loss (in Million $)",
        markers=True, color_discrete_sequence=["#58a6ff"],
        title="Tendência anual de perdas financeiras (M$)",
        template=TEMPLATE,
    )
    fig3.update_traces(fill="tozeroy", fillcolor="rgba(88,166,255,.15)")
    fig3.update_layout(plot_bgcolor="#161b22", paper_bgcolor="#0d1117")
    st.plotly_chart(fig3, use_container_width=True)

# ── Tab 2 · Financeiro ────────────────────────────────────────────────────────
with tab2:
    c1, c2 = st.columns(2)

    with c1:
        treemap_df = (
            df.groupby(["Attack Type", "Target Industry"], as_index=False)
            ["Financial Loss (in Million $)"].sum()
        )
        fig_tm = px.treemap(
            treemap_df,
            path=["Attack Type", "Target Industry"],
            values="Financial Loss (in Million $)",
            color="Financial Loss (in Million $)",
            color_continuous_scale="Reds",
            title="Treemap: perdas por tipo e setor",
            template=TEMPLATE,
        )
        fig_tm.update_layout(paper_bgcolor="#0d1117")
        st.plotly_chart(fig_tm, use_container_width=True)

    with c2:
        vuln_loss = (
            df.groupby("Security Vulnerability Type", as_index=False)
            ["Financial Loss (in Million $)"].sum()
            .sort_values("Financial Loss (in Million $)", ascending=False)
        )
        fig_v = px.bar(
            vuln_loss, x="Financial Loss (in Million $)", y="Security Vulnerability Type",
            orientation="h", color="Financial Loss (in Million $)",
            color_continuous_scale="Reds",
            title="Perda por tipo de vulnerabilidade",
            template=TEMPLATE,
        )
        fig_v.update_layout(showlegend=False, plot_bgcolor="#161b22", paper_bgcolor="#0d1117")
        st.plotly_chart(fig_v, use_container_width=True)

    # Scatter resolução × perda
    fig_sc = px.scatter(
        df, x="Incident Resolution Time (in Hours)", y="Financial Loss (in Million $)",
        color="Attack Type", size="Number of Affected Users",
        color_discrete_sequence=COLOR_SEQ,
        title="Resolução (h) × Perda financeira por incidente",
        template=TEMPLATE,
        opacity=0.7,
    )
    fig_sc.update_layout(plot_bgcolor="#161b22", paper_bgcolor="#0d1117")
    st.plotly_chart(fig_sc, use_container_width=True)

# ── Tab 3 · Geográfico ────────────────────────────────────────────────────────
with tab3:
    by_country_loss = (
        df.groupby("Country", as_index=False)["Financial Loss (in Million $)"].sum()
        .sort_values("Financial Loss (in Million $)", ascending=False)
    )
    fig_map = px.choropleth(
        by_country_loss, locations="Country", locationmode="country names",
        color="Financial Loss (in Million $)",
        color_continuous_scale="Reds",
        title="Perdas financeiras por país",
        template=TEMPLATE,
    )
    fig_map.update_layout(
        geo=dict(bgcolor="#0d1117", showframe=False),
        paper_bgcolor="#0d1117",
    )
    st.plotly_chart(fig_map, use_container_width=True)

    # Heatmap: ano × país (contagem de incidentes)
    pivot = df.pivot_table(index="Country", columns="Year", values="Financial Loss (in Million $)", aggfunc="sum", fill_value=0)
    fig_heat = go.Figure(
        go.Heatmap(
            z=pivot.values, x=[str(y) for y in pivot.columns], y=pivot.index,
            colorscale="Reds", showscale=True,
        )
    )
    fig_heat.update_layout(
        title="Heatmap de perdas: País × Ano",
        template=TEMPLATE,
        plot_bgcolor="#161b22", paper_bgcolor="#0d1117",
        height=600,
    )
    st.plotly_chart(fig_heat, use_container_width=True)

# ── Tab 4 · Mapa interativo ──────────────────────────────────────────────────
with tab4:
    st.markdown("**Clique em um país** para ver estatísticas detalhadas.")

    country_agg = (
        df.groupby("Country", as_index=False)
        .agg(
            incidentes=("Attack Type", "count"),
            perda_total=("Financial Loss (in Million $)", "sum"),
            usuarios=("Number of Affected Users", "sum"),
            resolucao_media=("Incident Resolution Time (in Hours)", "mean"),
        )
    )

    fig_interactive = px.choropleth(
        country_agg,
        locations="Country",
        locationmode="country names",
        color="perda_total",
        hover_name="Country",
        hover_data={
            "incidentes": True,
            "perda_total": ":,.0f",
            "usuarios": ":,",
            "resolucao_media": ":.1f",
            "Country": False,
        },
        color_continuous_scale="Reds",
        labels={
            "perda_total": "Perda (M$)",
            "incidentes": "Incidentes",
            "usuarios": "Usuários afetados",
            "resolucao_media": "Resolução média (h)",
        },
        title="Clique em um país para detalhar",
        template=TEMPLATE,
    )
    fig_interactive.update_layout(
        geo=dict(
            bgcolor="#0d1117",
            showframe=False,
            showcoastlines=True,
            coastlinecolor="#30363d",
            showland=True,
            landcolor="#161b22",
            showocean=True,
            oceancolor="#0d1117",
            showcountries=True,
            countrycolor="#30363d",
        ),
        paper_bgcolor="#0d1117",
        coloraxis_colorbar=dict(bgcolor="#161b22", tickcolor="#8b949e", title="Perda (M$)"),
        height=500,
        margin=dict(l=0, r=0, t=40, b=0),
    )

    map_event = st.plotly_chart(fig_interactive, use_container_width=True, on_select="rerun", selection_mode="points", key="map_select")

    selected_country_name = None
    if map_event and map_event.selection and map_event.selection.points:
        pt = map_event.selection.points[0]
        selected_country_name = pt.get("hovertext") or pt.get("location")

    if selected_country_name:
        c_df = df[df["Country"] == selected_country_name]
        st.markdown(f"### 📍 {selected_country_name}")

        d1, d2, d3, d4 = st.columns(4)
        d1.metric("Incidentes", f"{len(c_df):,}")
        d2.metric("Perda total (M$)", f"$ {c_df['Financial Loss (in Million $)'].sum():,.0f}")
        d3.metric("Usuários afetados", f"{int(c_df['Number of Affected Users'].sum()):,}")
        d4.metric("Resolução média (h)", f"{c_df['Incident Resolution Time (in Hours)'].mean():.1f}")

        st.markdown("<br>", unsafe_allow_html=True)
        ca, cb = st.columns(2)

        with ca:
            by_at = (
                c_df.groupby("Attack Type", as_index=False)["Financial Loss (in Million $)"]
                .sum()
                .sort_values("Financial Loss (in Million $)", ascending=False)
            )
            fig_c1 = px.bar(
                by_at, x="Financial Loss (in Million $)", y="Attack Type",
                orientation="h", color="Attack Type",
                color_discrete_sequence=COLOR_SEQ,
                title=f"Tipos de ataque — {selected_country_name}",
                template=TEMPLATE,
            )
            fig_c1.update_layout(showlegend=False, plot_bgcolor="#161b22", paper_bgcolor="#0d1117")
            st.plotly_chart(fig_c1, use_container_width=True)

        with cb:
            by_yr = (
                c_df.groupby("Year", as_index=False)["Financial Loss (in Million $)"]
                .sum()
                .sort_values("Year")
            )
            fig_c2 = px.area(
                by_yr, x="Year", y="Financial Loss (in Million $)",
                markers=True, color_discrete_sequence=["#f85149"],
                title=f"Evolução anual — {selected_country_name}",
                template=TEMPLATE,
            )
            fig_c2.update_traces(fill="tozeroy", fillcolor="rgba(248,81,73,.15)")
            fig_c2.update_layout(plot_bgcolor="#161b22", paper_bgcolor="#0d1117")
            st.plotly_chart(fig_c2, use_container_width=True)

        by_ind = (
            c_df.groupby("Target Industry", as_index=False)["Number of Affected Users"]
            .sum()
            .sort_values("Number of Affected Users", ascending=False)
        )
        fig_c3 = px.bar(
            by_ind, x="Target Industry", y="Number of Affected Users",
            color="Target Industry", color_discrete_sequence=COLOR_SEQ,
            title=f"Setores mais afetados — {selected_country_name}",
            template=TEMPLATE,
        )
        fig_c3.update_layout(showlegend=False, plot_bgcolor="#161b22", paper_bgcolor="#0d1117")
        st.plotly_chart(fig_c3, use_container_width=True)
    else:
        st.info("Clique em um país no mapa acima para ver análise detalhada.")

# ── Tab 5 · Dados brutos ──────────────────────────────────────────────────────
with tab5:
    st.markdown(f"**{len(df):,} registros** após filtros aplicados")
    st.dataframe(df.reset_index(drop=True), use_container_width=True, height=500)
