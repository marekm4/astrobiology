from rdkit import Chem
from rdkit.Chem import Draw, Descriptors

mol = Chem.MolFromSmiles('N')
print(Descriptors.MolWt(mol))
Draw.MolToImage(mol).save('out.png')
