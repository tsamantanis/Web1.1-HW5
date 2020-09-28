import pytest

from .app import app

#######################
# Index Tests
# (there's only one here because there is only one possible scenario!)
#######################

def test_index():
    """Test that the index page shows "Hello, World!" """
    res = app.test_client().get('/')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = "Hello, World!"
    assert expected_page_text == result_page_text


#######################
# Color Tests
#######################

def test_color_results_blue():
    """Test for color input blue"""
    result = app.test_client().get('/color_results?color=blue')
    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'Wow, blue is my favorite color, too!'
    assert expected_page_text == result_page_text

def test_color_results_scenario1():
    """Test for color input """
    result = app.test_client().get('/color_results?color=light%20green')
    assert result.status_code == 200
    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'Wow, light green is my favorite color, too!'
    assert expected_page_text == result_page_text

def test_color_results_edgecase1():
    """Test for empty color input"""
    result = app.test_client().get('/color_results?color=')
    assert result.status_code == 200
    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You did\'t specify a color!'
    assert expected_page_text == result_page_text


#######################
# Froyo Tests
#######################

def test_froyo_results_scenario1():
    """Test normal flavor and toppings input"""
    result = app.test_client().get('/froyo_results?flavor=strawberry&toppings=sprinkles')
    assert result.status_code == 200
    assert 'You ordered strawberry flavored Fro-Yo with toppings sprinkles!' in result.get_data(as_text=True)

def test_froyo_results_scenario2():
    result = app.test_client().get('/froyo_results?flavor=Banana&toppings=Chocolate%2C+Gummy+Bears')
    assert result.status_code == 200
    assert 'You ordered Banana flavored Fro-Yo with toppings Chocolate, Gummy Bears!' in result.get_data(as_text=True)


def test_froyo_results_edgecase1():
    """Test edge cases for empty flavor and toppings input"""
    result = app.test_client().get('/froyo_results?flavor=&toppings=')
    assert result.status_code == 200
    assert 'You didn\'t specify a flavor or any toppings!' in result.get_data(as_text=True)


def test_froyo_results_edgecase2():
    """Test edge cases for empty flavor or toppings input"""
    result = app.test_client().get('/froyo_results?flavor=&toppings=Chocolate%2C+Gummy+Bears')
    assert result.status_code == 200
    assert 'You didn\'t specify a flavor!' in result.get_data(as_text=True)

    result = app.test_client().get('/froyo_results?flavor=Banana&toppings=')
    assert result.status_code == 200
    assert 'You didn\'t specify any toppings!' in result.get_data(as_text=True)

#######################
# Reverse Message Tests
#######################

def test_message_results_helloworld():
    """Test normal input for reverse message"""
    form_data = {
        'message': 'Hello World'
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'dlroW olleH' in result_page_text

def test_message_results_scenario2():
    """Test long message input for reverse message"""
    form_data = {
        'message': 'Testing is not fun and it takes a very long time for no reason. Machines should be doing this!'
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200
    assert '!siht gniod eb dluohs senihcaM .nosaer on rof emit gnol yrev a sekat ti dna nuf ton si gnitseT' in res.get_data(as_text=True)

def test_message_results_edgecase1():
    """Test having any empty message input"""
    form_data = {
        'message': ''
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200
    assert 'You didn\'t add a message to reverse!' in res.get_data(as_text=True)



#######################
# Calculator Tests
#######################

def test_calculator_results_scenario1():
    """Test calculator results for add with normal input"""
    result = app.test_client().get('/calculator_results?operand1=2&operation=add&operand2=4')
    assert result.status_code == 200
    assert 'You chose to add 2 and 4. Your result is: 6' in result.get_data(as_text=True)

def test_calculator_results_scenario2():
    """Test calculator results for subtract with normal input"""
    result = app.test_client().get('/calculator_results?operand1=4&operation=subtract&operand2=2')
    assert result.status_code == 200
    assert 'You chose to subtract 4 and 2. Your result is: 2' in result.get_data(as_text=True)


def test_calculator_results_scenario3():
    """Test calculator results for multiply with normal input"""
    result = app.test_client().get('/calculator_results?operand1=-4&operation=multiply&operand2=2')
    assert result.status_code == 200
    assert 'You chose to multiply -4 and 2. Your result is: -8' in result.get_data(as_text=True)


def test_calculator_results_scenario4():
    """Test calculator results for multiply with normal input"""
    result = app.test_client().get('/calculator_results?operand1=4&operation=divide&operand2=2')
    assert result.status_code == 200
    assert 'You chose to divide 4 and 2. Your result is: 2' in result.get_data(as_text=True)


def test_calculator_results_edgecase1():
    """Test calculator results for empty operand input"""
    result = app.test_client().get('/calculator_results?operand1=&operation=divide&operand2=2')
    assert result.status_code == 200
    assert 'You didn\'t specify operand1!' in result.get_data(as_text=True)

    result = app.test_client().get('/calculator_results?operand1=2&operation=divide&operand2=')
    assert result.status_code == 200
    assert 'You didn\'t specify operand2!' in result.get_data(as_text=True)

def test_calculator_results_edgecase2():
    """Test calculator results for division by zero"""
    result = app.test_client().get('/calculator_results?operand1=2&operation=divide&operand2=0')
    assert result.status_code == 200
    assert 'You cannot divide by zero!' in result.get_data(as_text=True)

def test_calculator_results_edgecase3():
    """Test calculator results for not integer input"""
    result = app.test_client().get('/calculator_results?operand1=abc&operation=divide&operand2=0')
    assert result.status_code == 200
    assert 'Operands cannot be strings!' in result.get_data(as_text=True)
