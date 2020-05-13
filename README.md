# Spectral Forecast
Short description
------------------------------------------------------------
All the measurements are gathered using sensors applied to the skin of the patients. 
The prediction model uses three matrices: A for normal patients, B for diabetic patients and C which also contains normal patients, but 10 of them have predisposition to diabetes and the other 10 don't.
We have chosen to implement an example that computes the matrix M (which is used for predictions) and calculates S(d) (the similarity index).

Echipa formata din Calin Razvan si Suteu Mihaela, grupa 1241F
-------------------------------------------------------------------------------------------------------
An implementation after Paul A. Gagniuc et al. Spectral Forecast: A general purpose prediction model as
an alternative to classical neural networks.
Chaos 30, 033119 (2020); doi: 10.1063/1.5120818 https://aip.scitation.org/doi/pdf/10.1063/1.5120818
