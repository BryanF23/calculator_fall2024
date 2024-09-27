"""
This module contains tests for the Calculator REPL application.
"""

import pexpect


def test_repl_addition(repl: pexpect.spawn):
    """Test addition operation in the REPL."""
    repl.sendline('add 10 5')
    repl.expect(r'Result: 15\.0')
    repl.sendline('exit')
    repl.expect('Goodbye!')
    repl.expect(pexpect.EOF)

def test_repl_help(repl: pexpect.spawn):
    """Test the help command in the REPL."""
    repl.sendline('help')
    repl.expect('Available commands:')
    repl.expect(r'add a b.*Adds a and b')
    repl.sendline('exit')
    repl.expect('Goodbye!')
    repl.expect(pexpect.EOF)

def test_repl_invalid_command(repl: pexpect.spawn):
    """Test handling of an unknown command."""
    repl.sendline('unknown 1 2')
    repl.expect(r"Unknown operation 'unknown'.*")
    repl.sendline('exit')
    repl.expect('Goodbye!')
    repl.expect(pexpect.EOF)

def test_repl_division_by_zero(repl: pexpect.spawn):
    """Test division by zero handling."""
    repl.sendline('divide 10 0')
    repl.expect(r'Error: Division by zero\.')
    repl.sendline('exit')
    repl.expect('Goodbye!')
    repl.expect(pexpect.EOF)

def test_repl_invalid_numbers(repl: pexpect.spawn):
    """Test handling of invalid numeric input."""
    repl.sendline('add ten five')
    repl.expect(r'Invalid numbers\. Please enter valid numeric values\.')
    repl.sendline('exit')
    repl.expect('Goodbye!')
    repl.expect(pexpect.EOF)

def test_repl_multiple_operations(repl: pexpect.spawn):
    """Test multiple operations in a single REPL session."""
    repl.sendline('add 1 2')
    repl.expect(r'Result: 3\.0')
    repl.sendline('subtract 5 3')
    repl.expect(r'Result: 2\.0')
    repl.sendline('multiply 4 2')
    repl.expect(r'Result: 8\.0')
    repl.sendline('divide 9 3')
    repl.expect(r'Result: 3\.0')
    repl.sendline('exit')
    repl.expect('Goodbye!')
    repl.expect(pexpect.EOF)
