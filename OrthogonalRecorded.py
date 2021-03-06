# Script recorded by TexGen v3.10.0
weave = CTextileOrthogonal(6, 4, 3.8, 2.8, 0.35, 0.25, 1)
weave.SetWarpRatio( 2)
weave.SetBinderRatio( 1)
weave.SetWarpYarnWidths( 3.6)
weave.SetYYarnWidths( 2.58)
weave.SetBinderYarnWidths( 1.375)
weave.SetupLayers( 2, 3)
weave.SetGapSize( 0 )
weave.SetThickness( 1.5 )
weave.SetYarnLinearDensity( 0, 0, 'kg/m' )
weave.SetFibreDensity( 0, 0, 'kg/m^3' )
weave.SetFibreArea( 0, 0, 'm^2' )
weave.SetFibreDiameter( 0, 0.007, 'mm' )
weave.SetFibresPerYarn( 0, 5000 )
weave.SetYarnLinearDensity( 2, 0, 'kg/m' )
weave.SetFibreDensity( 2, 0, 'kg/m^3' )
weave.SetFibreArea( 2, 0, 'm^2' )
weave.SetFibreDiameter( 2, 0.007, 'mm' )
weave.SetFibresPerYarn( 2, 8000 )
weave.SetYarnLinearDensity( 1, 0, 'kg/m' )
weave.SetFibreDensity( 1, 0, 'kg/m^3' )
weave.SetFibreArea( 1, 0, 'm^2' )
weave.SetFibreDiameter( 1, 0.007, 'mm' )
weave.SetFibresPerYarn( 1, 3500 )
weave.SetMaxVolFraction( 0.78)
weave.SwapBinderPosition(0, 5)
weave.SwapBinderPosition(1, 2)
weave.SwapBinderPosition(2, 5)
weave.SwapBinderPosition(3, 2)
weave.SetWarpYarnPower( 0.6)
weave.SetWeftYarnPower( 0.6)
weave.SetBinderYarnPower( 0.8)
weave.SetXYarnWidths(0, 3.6)
weave.SetXYarnHeights(0, 0.35)
weave.SetXYarnSpacings(0, 3.8)
weave.SetXYarnWidths(1, 3.6)
weave.SetXYarnHeights(1, 0.35)
weave.SetXYarnSpacings(1, 3.8)
weave.SetXYarnWidths(2, 1.375)
weave.SetXYarnHeights(2, 0.16)
weave.SetXYarnSpacings(2, 1.4)
weave.SetXYarnWidths(3, 3.6)
weave.SetXYarnHeights(3, 0.35)
weave.SetXYarnSpacings(3, 3.8)
weave.SetXYarnWidths(4, 3.6)
weave.SetXYarnHeights(4, 0.35)
weave.SetXYarnSpacings(4, 3.8)
weave.SetXYarnWidths(5, 1.375)
weave.SetXYarnHeights(5, 0.16)
weave.SetXYarnSpacings(5, 1.4)
weave.SetYYarnWidths(0, 2.58)
weave.SetYYarnHeights(0, 0.25)
weave.SetYYarnSpacings(0, 2.8)
weave.SetYYarnWidths(1, 2.58)
weave.SetYYarnHeights(1, 0.25)
weave.SetYYarnSpacings(1, 2.8)
weave.SetYYarnWidths(2, 2.58)
weave.SetYYarnHeights(2, 0.25)
weave.SetYYarnSpacings(2, 2.8)
weave.SetYYarnWidths(3, 2.58)
weave.SetYYarnHeights(3, 0.25)
weave.SetYYarnSpacings(3, 2.8)
weave.AssignDefaultDomain()
weave.SetDomainZValues()
textilename = AddTextile(weave)

