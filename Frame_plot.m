% This script prepares the javaplex library for use


javaaddpath('javaplex.jar');
import edu.stanford.math.plex4.*;

javaaddpath('plex-viewer.jar');
import edu.stanford.math.plex_viewer.*;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      
data=pdb2mat('C60.pdb');  %%%%%%%%%% read in the PDB data
options.filename = 'C60';
     
[dim,num]=size(data.X);
atom(:,1)=data.X;
atom(:,2)=data.Y;
atom(:,3)=data.Z;

min_dimension = 1;
max_dimension = 3;
max_filtration_value = 6.2;
num_divisions = 10000;

% create the set of points
point_cloud = atom;

% create a Vietoris-Rips stream 
stream = api.Plex4.createVietorisRipsStream(point_cloud, max_dimension, max_filtration_value, num_divisions);

% get persistence algorithm over Z/2Z
persistence = api.Plex4.getModularSimplicialAlgorithm(max_dimension, 2);

% compute the intervals
intervals = persistence.computeIntervals(stream);

% create the barcode plots
options.max_filtration_value = max_filtration_value;
options.min_dimension = min_dimension - 1;
options.max_dimension = max_dimension - 1;
plot_barcode_java(intervals, options);


