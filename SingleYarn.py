# Python script for ICMAC workshop slides

# Create empty textile with one yarn
Textile = CTextile()
Yarn = CYarn()

# Add nodes to yarn
Yarn.AddNode(CNode(XYZ(0,0,0)))
Yarn.AddNode(CNode(XYZ(5,0,1)))
Yarn.AddNode(CNode(XYZ(10,0,0)))

# Assign interpolation method for joining nodes
Yarn.AssignInterpolation(CInterpolationCubic())

# Create class to add sections at each node and interpolate between them
YarnSections = CYarnSectionInterpNode()
YarnSections.AddSection( CSectionLenticular(1.0,0.5,0.1) )
YarnSections.AddSection( CSectionPowerEllipse(1.0,0.5,0.4,0.25) )

# Hybrid Section
Top = CSectionEllipse( 1.0, 0.4 )
Bottom = CSectionPowerEllipse( 1.0, 0.4, 0.4, 0.25 )
YarnSections.AddSection( CSectionHybrid( Top, Bottom ) )

# Add the sections to the yarn
Yarn.AssignSection( YarnSections )

# Repeat yarn in both x and y directions
Yarn.AddRepeat(XYZ(10,0,0))
Yarn.AddRepeat(XYZ(5,5,0))

# Add the yarn to the textile
Textile.AddYarn(Yarn)

# Repeat yarn in both x and y directions
Yarn.AddRepeat(XYZ(10,0,0))
Yarn.AddRepeat(XYZ(5,5,0))

# Set up a domain specifying two opposite corners of box
Textile.AssignDomain(CDomainPlanes(XYZ(-5,-2,-1),XYZ(15,12,2)))

# Add the textile to the TexGen list
AddTextile("Workshop", Textile)
