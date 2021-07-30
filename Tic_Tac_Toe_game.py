import streamlit as st

st.set_page_config('Tic Tac Toe','Tic_logo.png',initial_sidebar_state='collapsed')
# max top padding
top_padding_style = st.markdown("""
<style>
.css-hi6a2p {padding-top: 0rem;}
</style>
""", unsafe_allow_html=True)


# Hide Streamlit Promotions
hide_streamlit_style = st.markdown("""
            <style>
            #MainMenu {visibility: visible;}
            footer {visibility: hidden;}
            footer {
                visibility: hidden;
            }
            footer:after {
                content:'✖️Tic Tac Toe ⭕';
                visibility: visible;
                display: block;
                position: relative;
                color: grey;
            }
            </style>
            """, unsafe_allow_html=True)

# Tic Tac Toe style Text
tictactoe_style = st.markdown('''<div
     style="background-image: linear-gradient(to left,#36363D,black, #36363D);padding:10px;border-radius:25px">
    <h2
    style="color:grey;text-align:center;font-size:20px"> TIK TAC TOE
    </h2>
    </div> ''', unsafe_allow_html=True)

st.text('')
st.text('')
st.text('')
select_game_layout = st.sidebar.selectbox('',['Desktop Layout','Phone Layout'])
if select_game_layout == 'Desktop Layout':
    # button Design For pc Layout
    Button_Design_pc = st.markdown("""
    <style>
    div.stButton> button:first-child{
        color:  white;
        background: black;
        border-color:black;
        background-size: 500%;
        transition: 0.3s ;
        border-radius:7px;
        font-size:45px;
        font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
        position:relative;left:32%;
    }
    div.stButton:hover> button:first-child  {
        background-position: left;
        border-radius:40px;
        border-color:white;
        color: white;
        font-size:45px;
        font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
        position:relative;left:32%;
    }
    </style>""", unsafe_allow_html=True)

    # Initiating the states
    if '1' not in st.session_state:
        st.session_state.turn = '✖️'
        st.session_state.one = '➖'
        st.session_state.two = '➖'
        st.session_state.three = '➖'
        st.session_state.four = '➖'
        st.session_state.five = '➖'
        st.session_state.six = '➖'
        st.session_state.seven = '➖'
        st.session_state.eight = '➖'
        st.session_state.nine = '➖'
        st.session_state.scorex = 0
        st.session_state.scoreo = 0
        st.session_state.game_over = ''


    def non():
        if st.session_state.game_over == '':
            if st.session_state.one == '➖':
                st.session_state.one = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def ntwo():
        if st.session_state.game_over == '':
            if st.session_state.two == '➖':
                st.session_state.two = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def nthree():
        if st.session_state.game_over == '':
            if st.session_state.three == '➖':
                st.session_state.three = st.session_state.turn

                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def nfour():
        if st.session_state.game_over == '':
            if st.session_state.four == '➖':
                st.session_state.four = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def nfive():
        if st.session_state.game_over == '':
            if st.session_state.five == '➖':
                st.session_state.five = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def nsix():
        if st.session_state.game_over == '':
            if st.session_state.six == '➖':
                st.session_state.six = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def nseven():
        if st.session_state.game_over == '':
            if st.session_state.seven == '➖':
                st.session_state.seven = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def neight():
        if st.session_state.game_over == '':
            if st.session_state.eight == '➖':
                st.session_state.eight = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def nnine():
        if st.session_state.game_over == '':
            if st.session_state.nine == '➖':
                st.session_state.nine = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'

    def restart():
        st.session_state.turn = '✖️'
        st.session_state.one = '➖'
        st.session_state.two = '➖'
        st.session_state.three = '➖'
        st.session_state.four = '➖'
        st.session_state.five = '➖'
        st.session_state.six = '➖'
        st.session_state.seven = '➖'
        st.session_state.eight = '➖'
        st.session_state.nine = '➖'
        st.session_state.game_over = ''

    b1, b2, b3 = st.beta_columns(3)

    one = b1.button(st.session_state.one, key='1', on_click=non)
    two = b2.button(st.session_state.two, key='2', on_click=ntwo)
    three = b3.button(st.session_state.three, key='3', on_click=nthree)
    four = b1.button(st.session_state.four, key='4', on_click=nfour)
    five = b2.button(st.session_state.five, key='5', on_click=nfive)
    six = b3.button(st.session_state.six, key='6', on_click=nsix)
    seven = b1.button(st.session_state.seven, key='7', on_click=nseven)
    eight = b2.button(st.session_state.eight, key='8', on_click=neight)
    nine = b3.button(st.session_state.nine, key='9', on_click=nnine)

    if st.session_state.one == st.session_state.two == st.session_state.three != '➖' or st.session_state.four == st.session_state.five == st.session_state.six != '➖'\
            or st.session_state.seven == st.session_state.eight == st.session_state.nine != '➖' or st.session_state.one == st.session_state.five == st.session_state.nine != '➖'\
            or st.session_state.three == st.session_state.five == st.session_state.seven != '➖' or st.session_state.one == st.session_state.four == st.session_state.seven != '➖'\
            or st.session_state.two == st.session_state.five == st.session_state.eight != '➖' or st.session_state.three == st.session_state.six == st.session_state.nine != '➖':
        if st.session_state.game_over == '':
            if st.session_state.turn == '✖️':
                st.session_state.turn = '⭕'
                st.session_state.scoreo+=1
            else:
                st.session_state.turn = '✖️'
                st.session_state.scorex+=1
        st.session_state.game_over = True
        st.markdown(f'''<div
        style="background-color:black;padding:10px;border-radius:9px">
        <h2
        style="color:grey;text-align:center;font-size:20px">Winner is {st.session_state.turn}
        </h2>
        </div> ''',unsafe_allow_html=True)
        st.balloons()
        l1,l2,l3 = st.beta_columns([1,3,1])
        restart_button = l2.button('Restart',on_click=restart,key='10')

    if st.session_state.one != '➖' and st.session_state.two != '➖' and st.session_state.three != '➖' and st.session_state.four != '➖' \
            and st.session_state.five != '➖' and st.session_state.six != '➖' and st.session_state.seven != '➖' and st.session_state.eight != '➖' and st.session_state.nine != '➖' and st.session_state.game_over!=True:
        l1, l2, l3 = st.beta_columns([1, 3, 1])
        restart_button = l2.button('Restart',on_click=restart,key='11')
        st.markdown(f'''<div
            style="background-color:black;padding:10px;border-radius:9px">
            <h2
            style="color:grey;text-align:center;font-size:20px">Its a Tie !!!
            </h2>
            </div> ''', unsafe_allow_html=True)

    st.markdown(f'''<div
        style="background-color:black;padding:10px;border-radius:9px">
        <h2
        style="color:grey;text-align:left;font-size:20px">Player ✖️- {str(st.session_state.scorex)} ━━━━━━━━━━━━━━━━━━━━━ Player ⭕ - {str(st.session_state.scoreo)}
        </h2>
        </div> ''',unsafe_allow_html=True)

elif select_game_layout == 'Phone Layout':
    # button Design For pc Layout
    Button_Design_Phone = st.markdown("""
        <style>
        div.stButton> button:first-child{

            color:  white;
            background: black;
            border-color:black;
            background-size: 500%;
            transition: 0.3s ;
            border-radius:7px;
            font-size:25px;
            font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
            position:relative;left:22%;
        }
        div.stButton:hover> button:first-child  {
            background-position: left;
            border-radius:40px;
            border-color:white;
            color: white;
            font-size:25px;
            font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
            position:relative;left:22%;
        }
        </style>""", unsafe_allow_html=True)
    # Initiating the states
    if '1' not in st.session_state:
        st.session_state.turn = '✖️'
        st.session_state.one = '➖'
        st.session_state.two = '➖'
        st.session_state.three = '➖'
        st.session_state.four = '➖'
        st.session_state.five = '➖'
        st.session_state.six = '➖'
        st.session_state.seven = '➖'
        st.session_state.eight = '➖'
        st.session_state.nine = '➖'
        st.session_state.scorex = 0
        st.session_state.scoreo = 0
        st.session_state.game_over = ''


    def non():
        if st.session_state.game_over == '':
            if st.session_state.one == '➖':
                st.session_state.one = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def ntwo():
        if st.session_state.game_over == '':
            if st.session_state.two == '➖':
                st.session_state.two = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def nthree():
        if st.session_state.game_over == '':
            if st.session_state.three == '➖':
                st.session_state.three = st.session_state.turn

                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def nfour():
        if st.session_state.game_over == '':
            if st.session_state.four == '➖':
                st.session_state.four = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def nfive():
        if st.session_state.game_over == '':
            if st.session_state.five == '➖':
                st.session_state.five = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def nsix():
        if st.session_state.game_over == '':
            if st.session_state.six == '➖':
                st.session_state.six = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def nseven():
        if st.session_state.game_over == '':
            if st.session_state.seven == '➖':
                st.session_state.seven = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def neight():
        if st.session_state.game_over == '':
            if st.session_state.eight == '➖':
                st.session_state.eight = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def nnine():
        if st.session_state.game_over == '':
            if st.session_state.nine == '➖':
                st.session_state.nine = st.session_state.turn
                if st.session_state.turn == '✖️':
                    st.session_state.turn = '⭕'
                else:
                    st.session_state.turn = '✖️'


    def restart():
        st.session_state.turn = '✖️'
        st.session_state.one = '➖'
        st.session_state.two = '➖'
        st.session_state.three = '➖'
        st.session_state.four = '➖'
        st.session_state.five = '➖'
        st.session_state.six = '➖'
        st.session_state.seven = '➖'
        st.session_state.eight = '➖'
        st.session_state.nine = '➖'
        st.session_state.game_over = ''

    b1, b2, b3, b4, b5, b6, b7, b8, b9 = st.beta_columns(9)

    one = b1.button(st.session_state.one, key='1', on_click=non)
    two = b2.button(st.session_state.two, key='2', on_click=ntwo)
    three = b3.button(st.session_state.three, key='3', on_click=nthree)
    four = b1.button(st.session_state.four, key='4', on_click=nfour)
    five = b2.button(st.session_state.five, key='5', on_click=nfive)
    six = b3.button(st.session_state.six, key='6', on_click=nsix)
    seven = b1.button(st.session_state.seven, key='7', on_click=nseven)
    eight = b2.button(st.session_state.eight, key='8', on_click=neight)
    nine = b3.button(st.session_state.nine, key='9', on_click=nnine)

    if st.session_state.one == st.session_state.two == st.session_state.three != '➖' or st.session_state.four == st.session_state.five == st.session_state.six != '➖' \
            or st.session_state.seven == st.session_state.eight == st.session_state.nine != '➖' or st.session_state.one == st.session_state.five == st.session_state.nine != '➖' \
            or st.session_state.three == st.session_state.five == st.session_state.seven != '➖' or st.session_state.one == st.session_state.four == st.session_state.seven != '➖' \
            or st.session_state.two == st.session_state.five == st.session_state.eight != '➖' or st.session_state.three == st.session_state.six == st.session_state.nine != '➖':
        if st.session_state.game_over == '':
            if st.session_state.turn == '✖️':
                st.session_state.turn = '⭕'
                st.session_state.scoreo += 1
            else:
                st.session_state.turn = '✖️'
                st.session_state.scorex += 1
        st.session_state.game_over = True
        st.markdown(f'''<div
            style="background-color:black;padding:10px;border-radius:9px">
            <h2
            style="color:grey;text-align:left;font-size:20px">Winner is {st.session_state.turn}
            </h2>
            </div> ''', unsafe_allow_html=True)
        st.balloons()
        restart_button = st.button('🆑 Restart 🆑',on_click=restart)

    if st.session_state.one != '➖' and st.session_state.two != '➖' and st.session_state.three != '➖' and st.session_state.four != '➖' \
            and st.session_state.five != '➖' and st.session_state.six != '➖' and st.session_state.seven != '➖' and st.session_state.eight != '➖' and st.session_state.nine != '➖' and st.session_state.game_over!=True:
        l1,l2,l3 = st.beta_columns([1,3,1])
        restart_button = l1.button('Restart',on_click=restart)
        st.markdown(f'''<div
                    style="background-color:black;padding:10px;border-radius:9px">
                    <h2
                    style="color:grey;text-align:center;font-size:20px">Its a Tie !!!
                    </h2>
                    </div> ''', unsafe_allow_html=True)

    st.markdown(f'''<div
            style="background-color:black;padding:10px;border-radius:9px">
            <h2
            style="color:grey;text-align:left;font-size:20px">Player ✖️- {str(st.session_state.scorex)}  ━━━  Player ⭕ - {str(st.session_state.scoreo)}
            </h2>
            </div> ''', unsafe_allow_html=True)
