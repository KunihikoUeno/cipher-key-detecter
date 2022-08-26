# Cipher Key Detecter

## Usage

```python
python cipher-key-detecter.py {original_text} {encrypted_text}
```

Make sure to reorganize the key you get.

### Example

If the output is `ecinfos`, the key can be possibly 7 values.

1. `ecinfos`
1. `secinfo`
1. `osecinf`
1. `fosecin`
1. `nfoseci`
1. `infosec`
1. `cinfose`

Try them all until you get the correct key.
