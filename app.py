from random import choice

import pandas as pd
import streamlit as st

ONE = "dále'é"
TWO = "naaki"
THREE = "tai'"
FOUR = "dį́į́'"
FIVE = "ąąshdlai'"
SIX = "guustáni"
SEVEN = "guusts'iidi"
EIGHT = "tsąąbi'"
NINE = "ńguust'ai'"
TEN = "guneenani"

AFFIX_ONE = "łe"
SUFFIX_TEN = "dzáa'da"

TWENTY = "naadini"
THIRTY = "tàdini"
FORTY = f"{FOUR[:-1]}shdini"
FIFTY = f"{FIVE[:-2]}dini"
SIXTY = f"{SIX[:5]}ą́dini"
SEVENTY = f"{SEVEN}dini"

BINGO: dict[str, dict[int, str]] = {
    "B": {
        1: ONE,
        2: TWO,
        3: THREE,
        4: FOUR,
        5: FIVE,
        6: SIX,
        7: SEVEN,
        8: EIGHT,
        9: NINE,
        10: TEN,
        11: f"{AFFIX_ONE} {SUFFIX_TEN}",
        12: f"{TWO} {SUFFIX_TEN}",
        13: f"{THREE} {SUFFIX_TEN}",
        14: f"{FOUR} {SUFFIX_TEN}",
        15: f"{FIVE} {SUFFIX_TEN}",
    },
    "I": {
        16: f"{SIX} {SUFFIX_TEN}",
        17: f"{SEVEN} {SUFFIX_TEN}",
        18: f"{EIGHT} {SUFFIX_TEN}",
        19: f"{NINE} {SUFFIX_TEN}",
        20: TWENTY,
        21: f"{TWENTY} {AFFIX_ONE}",
        22: f"{TWENTY} {TWO}",
        23: f"{TWENTY} {THREE}",
        24: f"{TWENTY} {FOUR}",
        25: f"{TWENTY} {FIVE}",
        26: f"{TWENTY} {SIX}",
        27: f"{TWENTY} {SEVEN}",
        28: f"{TWENTY} {EIGHT}",
        29: f"{TWENTY} {NINE}",
        30: THIRTY,
    },
    "N": {
        31: f"{THIRTY} {AFFIX_ONE}",
        32: f"{THIRTY} {TWO}",
        33: f"{THIRTY} {THREE}",
        34: f"{THIRTY} {FOUR}",
        35: f"{THIRTY} {FIVE}",
        36: f"{THIRTY} {SIX}",
        37: f"{THIRTY} {SEVEN}",
        38: f"{THIRTY} {EIGHT}",
        39: f"{THIRTY} {NINE}",
        40: FORTY,
        41: f"{FORTY} {AFFIX_ONE}",
        42: f"{FORTY} {TWO}",
        43: f"{FORTY} {THREE}",
        44: f"{FORTY} {FOUR}",
        45: f"{FORTY} {FIVE}",
    },
    "G": {
        46: f"{FORTY} {SIX}",
        47: f"{FORTY} {SEVEN}",
        48: f"{FORTY} {EIGHT}",
        49: f"{FORTY} {NINE}",
        50: FIFTY,
        51: f"{FIFTY} {AFFIX_ONE}",
        52: f"{FIFTY} {TWO}",
        53: f"{FIFTY} {THREE}",
        54: f"{FIFTY} {FOUR}",
        55: f"{FIFTY} {FIVE}",
        56: f"{FIFTY} {SIX}",
        57: f"{FIFTY} {SEVEN}",
        58: f"{FIFTY} {EIGHT}",
        59: f"{FIFTY} {NINE}",
        60: SIXTY,
    },
    "O": {
        61: f"{SIXTY} {AFFIX_ONE}",
        62: f"{SIXTY} {TWO}",
        63: f"{SIXTY} {THREE}",
        64: f"{SIXTY} {FOUR}",
        65: f"{SIXTY} {FIVE}",
        66: f"{SIXTY} {SIX}",
        67: f"{SIXTY} {SEVEN}",
        68: f"{SIXTY} {EIGHT}",
        69: f"{SIXTY} {NINE}",
        70: SEVENTY,
        71: f"{SEVENTY} {AFFIX_ONE}",
        72: f"{SEVENTY} {TWO}",
        73: f"{SEVENTY} {THREE}",
        74: f"{SEVENTY} {FOUR}",
        75: f"{SEVENTY} {FIVE}",
    },
}

RULES = [
    "75-Ball Bingo",
    "",
    "Players use cards that feature five columns of five squares each, with every square containing a number (except the middle square, which is designated a 'FREE' space). A player wins by completing a row, column, or diagonal.",
    "",
    "Columns:",
    "   B: numbers 1 through 15",
    "   I: numbers 16 through 30",
    "   N: numbers 31 through 45",
    "   G: numbers 46 through 60",
    "   O: numbers 61 through 75",
    "",
    "The number of all possible bingo card variations is 552,446,474,061,128,648,601,600.",
]


def generate_bingo_draw(
    bingo_numbers: dict[str, dict[int, str]],
) -> tuple[str, int, str] | None:
    """Draw a random bingo number from the BINGO card."""
    # Filter columns that still have numbers left
    available_columns = [col for col, nums in bingo_numbers.items() if nums]
    if not available_columns:
        return None
    column = choice(available_columns)
    number, translation = choice(list(bingo_numbers[column].items()))
    return column, number, translation


def main():
    title = "Ndé Bizaa' Bingo"
    st.set_page_config(page_title=title, page_icon="🪶")
    st.title(f"{title} 🪶")
    if "bingo_numbers" not in st.session_state:
        st.session_state.bingo_numbers = BINGO.copy()
    if "drawn_numbers" not in st.session_state:
        st.session_state.drawn_numbers = []
    if "display_balloons" not in st.session_state:
        st.session_state.display_balloons = True

    if st.button("Draw a Bingo Number"):
        if st.session_state.bingo_numbers:
            bingo_items = generate_bingo_draw(st.session_state.bingo_numbers)
            if bingo_items is None:
                st.session_state.bingo_numbers = None
            else:
                column, number, translation = bingo_items
                st.session_state.drawn_numbers.append((column, number, translation))
                st.session_state.bingo_numbers[column].pop(number)

                st.header(f"{column} {number}")
                st.subheader(f"{number}: {translation}")

    if st.session_state.bingo_numbers is None:
        if st.session_state.display_balloons:
            st.balloons()
            st.session_state.display_balloons = False
        st.info("All Bingo numbers have been drawn!")

    if not st.session_state.drawn_numbers:
        st.markdown(":blue[Press the button to draw a Bingo number.]")
    elif st.session_state.bingo_numbers:
        st.markdown(":green[Press the button to draw another Bingo number.]")

    display_button = st.button("Display BINGO Rules")

    if st.button("Reset"):
        st.session_state.bingo_numbers = BINGO.copy()
        st.session_state.drawn_numbers = []
        st.session_state.display_balloons = True
        st.info("The Bingo game has been reset. You can start drawing numbers again.")

    if display_button:
        # st.subheader(RULES[0])
        # for rule in RULES[1:]:
        #     st.write(rule)
        # st.text_area("BINGO Rules", value="\n".join(RULES), height=200)
        st.code(
            "\n".join(RULES),
            language=None,
            wrap_lines=True,
        )
    st.divider()

    if st.session_state.drawn_numbers:
        drawn_numbers = [
            (f"{col} {num}", trans)
            for col, num, trans in st.session_state.drawn_numbers
        ]
        data = pd.DataFrame(drawn_numbers, columns=["Bingo Number", "Translation"])
        st.write("History:")
        st.data_editor(data)


if __name__ == "__main__":
    main()
