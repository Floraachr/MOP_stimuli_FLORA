# **Syllable Generator for Conlangs**
## by Golden Gold

------

- **Consonant Groups** can be created in the `'groups.txt'` file.
  - Syntax: `GroupName: l1, l2, l3, ...`.
  - Divide groups with new line.
  
- **Rules** can be created in the `'rules.txt'` file:
  - `A~B`: group `B` must appear after group `A`.
  - `A!B`: group `B` cannot appear after group `A`.
  - Divide rules with new line.


### Options:
- `'structure'`: syllable structure: 
	- `'*'` before group name means it is mandatory.
	- Divide groups with `','` (spaces do not matter).

- `'syllables'`: amount of syllables to create.
- `'display'`: how to display the syllables in the console:
	- `'{index}'`: the syllable's index.
	- `'{syllable}'`:  the syllable itself.
	- `'\n'`: new line.

> If you get an `IndexError`, it's because your rules are not compatible with each other. For example, you set the rule `N!N` (nasals can't follow nasals), but your syllable structure is `CVNC`. and nasals are included as all consonants.

## \*Just download the source code, there is no release 
