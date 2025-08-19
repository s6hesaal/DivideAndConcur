from PlotCreator import plotRuns


plotRuns("Outputs/LCP", "./Plots/LCP", 0, [500, 1000, 5000],
         [{"key": "dr", "label": "Divide and Concur with Douglas-Rachford"},
          {"key": "ap", "label": "Divide and Concur with alternating projections"}],
         lambda name, m, n: "Solve LCP for %s - a %dx%d matrix" % (name, m, n))

plotRuns("Outputs/MatrixScaling", "./Plots/MatrixScaling", 1, [50, 100],
         [{"key": "sinkhorn", "label": "Sinkhorn-Knopp"},
          {"key": "dc_ap", "label": "Divide and Concur with alternating projections"}],
         lambda name, m, n: "Solve matrix scaling for %s - a %dx%d matrix" % (name, m, n))


plotRuns("Outputs/LP", "./Plots/LP", 0, [500, 1000, 5000],
         [{"key": "dr", "label": "Divide and Concur with Douglas-Rachford"},
          {"key": "ap", "label": "Divide and Concur with alternating projections"},
          {"key": "nesterov", "label": "Nesterov's accelerated gradient decent"}],
         lambda name, m, n: r"Solve $Ax\leq b$ for %s - a %dx%d matrix." % (name, m, n))

plotRuns("Outputs/EqualsAsInequality", "./Plots/EqualsAsInequality", 0, [500, 1000],
         [{"key": "dr", "label": "Divide and Concur with Douglas-Rachford"},
          {"key": "ap", "label": "Divide and Concur with alternating projections"},
          {"key": "nesterov", "label": "Nesterov's accelerated gradient decent"}],
         lambda name, m, n: r"Solve $Ax\leq b$ for %s - a %dx%d matrix." % (name, m, n))

plotRuns("Outputs/Equals", "./Plots/Equals", 0, [500, 1000],
         [{"key": "dr", "label": "Divide and Concur with Douglas-Rachford"},
          {"key": "ap", "label": "Divide and Concur with alternating projections"},
          {"key": "nesterov", "label": "Nesterov's accelerated gradient decent"}],
         lambda name, m, n: r"Solve $Ax = b$ for %s - a %dx%d matrix." % (name, m, n))
