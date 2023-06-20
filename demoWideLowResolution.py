# %%
from source.classBP import BeamPattern

# %%
####### Generate a test Wide Beam Pattern with default values #######

WB = BeamPattern(BPtype='Wide', Ncycles=3, factor=0.3, step=0.5, Ndepth=200, NelImm=50)

# Compute maps
WB.MapsCompute()

# Option to save the maps 
# NB.SaveMaps('testData/LowWide.pkl')

# If maps are precomputed you can reload them
# NB.LoadMaps('testData/LowWide.pkl')

#%%
# If maps are loaded you want to change delays profile by defining a different focus or number
# of active elements or both
WB.beam["active_el"] = [15, 20]
WB.beam["focus"] = [10e-3, 30e-3]
WB.DelaysSet()

# Computation and display of BP
WB.BPcompute()
WB.BPplot(3)
# %%
