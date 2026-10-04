import streamlit as st

if "display" not in st.session_state:
    st.session_state.display = ""
if "expression" not in st.session_state:
    st.session_state.expression = ""
if "first_number" not in st.session_state:
    st.session_state.first_number = None
if "operation" not in st.session_state:
    st.session_state.operation = None
if "new_number" not in st.session_state:
    st.session_state.new_number = True

def number_click(number):
    if st.session_state.new_number:
        st.session_state.display = str(number)
        st.session_state.new_number = False
    else:
        st.session_state.display += str(number)
    st.session_state.expression = st.session_state.expression + str(number)

def decimal_click():
    if st.session_state.new_number:
        st.session_state.display = "0."
        st.session_state.expression += "0."
        st.session_state.new_number = False
    elif "." not in st.session_state.display:
        st.session_state.display += "."
        st.session_state.expression += "."
        
def operation_click(operation):
    if st.session_state.display == "":
        return
    if st.session_state.first_number is not None:
        calculate()
    st.session_state.first_number = float(st.session_state.display)
    st.session_state.operation = operation
    st.session_state.new_number = True
    st.session_state.expression += " " + operation + " "

def calculate():
    if st.session_state.first_number is None:
        return
    if st.session_state.display == "":
        return
    second_number = float(st.session_state.display)
    first_number = st.session_state.first_number
    operation = st.session_state.operation
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "×":
        result = first_number * second_number
    elif operation == "÷":
        if second_number == 0:
            st.session_state.display = "Error"
            st.session_state.expression = "Cannot divide by zero"
            st.session_state.first_number = None
            st.session_state.operation = None
            return
        result = first_number / second_number
    if result == int(result):
        result = int(result)
    st.session_state.display = str(result)
    st.session_state.expression = str(result)
    st.session_state.first_number = None
    st.session_state.operation = None
    st.session_state.new_number = True

def clear():
    st.session_state.display = ""
    st.session_state.expression = ""
    st.session_state.first_number = None
    st.session_state.operation = None
    st.session_state.new_number = True

def backspace():
    if st.session_state.display != "":
        st.session_state.display = st.session_state.display[:-1]
        if st.session_state.expression != "":
            st.session_state.expression = st.session_state.expression[:-1]

st.title("Calculator")
st.text_input(
    "Expression",
    value=st.session_state.expression,
    disabled=True
)

#Row 1 
row1 = st.columns(4)
row1[0].button(
    "AC",
    use_container_width=True,
    on_click=clear
)
row1[1].button(
    "⌫",
    use_container_width=True,
    on_click=backspace
)
row1[2].button(
    "÷",
    use_container_width=True,
    on_click=operation_click,
    args=("÷",)
)
row1[3].button(
    "×",
    use_container_width=True,
    on_click=operation_click,
    args=("×",)
)

# Row 2
row2 = st.columns(4)
row2[0].button(
    "7",
    use_container_width=True,
    on_click=number_click,
    args=(7,)
)
row2[1].button(
    "8",
    use_container_width=True,
    on_click=number_click,
    args=(8,)
)
row2[2].button(
    "9",
    use_container_width=True,
    on_click=number_click,
    args=(9,)
)
row2[3].button(
    "-",
    use_container_width=True,
    on_click=operation_click,
    args=("-",)
)

# Row 3
row3 = st.columns(4)
row3[0].button(
    "4",
    use_container_width=True,
    on_click=number_click,
    args=(4,)
)
row3[1].button(
    "5",
    use_container_width=True,
    on_click=number_click,
    args=(5,)
)
row3[2].button(
    "6",
    use_container_width=True,
    on_click=number_click,
    args=(6,)
)
row3[3].button(
    "+",
    use_container_width=True,
    on_click=operation_click,
    args=("+",)
)

# Row 4
row4 = st.columns(4)
row4[0].button(
    "1",
    use_container_width=True,
    on_click=number_click,
    args=(1,)
)
row4[1].button(
    "2",
    use_container_width=True,
    on_click=number_click,
    args=(2,)
)
row4[2].button(
    "3",
    use_container_width=True,
    on_click=number_click,
    args=(3,)
)
row4[3].button(
    "=",
    use_container_width=True,
    on_click=calculate
)

# Row 5
row5 = st.columns(3)
row5[0].button(
    "0",
    use_container_width=True,
    on_click=number_click,
    args=(0,)
)
row5[1].button(
    ".",
    use_container_width=True,
    on_click=decimal_click
)
row5[2].button(
    "C",
    use_container_width=True,
    on_click=clear
)
