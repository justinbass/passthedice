# passthedice
Generate random cryptocurrency private keys from dice rolls

Generates using the provably lowest number of dice rolls for a given key.

Example for generating iota key with a d20:

```python passthedice.py -c iota -d 20```

Example for generating a bitcoin private key with Python's random implementation:

```python passthedice.py -c bitcoin -r```

Output:

```Private key: 6701EDF05F7BBCFD5522A219AD821977E6B2EBB1C7E155EF19965F821D884782```

For all options:

```python passthedice.py --help```
