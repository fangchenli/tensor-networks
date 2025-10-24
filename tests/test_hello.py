"""Basic tests for the tensor_networks package."""

from tensor_networks import hello


def test_hello():
    """Test the hello function."""
    result = hello()
    assert result == "Hello from tensor-networks!"
    assert isinstance(result, str)
