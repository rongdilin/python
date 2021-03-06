#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 17:21:38 2017

@author: rongdilin
"""

#from Sudoku import Sudoku
from tex import latex2pdf
document = ur"""
        \documentclass[10pt]{article}
\\usepackage[left=0pt,right=0pt]{geometry}
\\usepackage{tikz}
\\usetikzlibrary{positioning}
\\usepackage{cancel}
\pagestyle{empty}

\newcommand{\N}[5]{\tikz{\node[label=above left:{\tiny #1},
                               label=above right:{\tiny #2},
                               label=below left:{\tiny #3},
                               label=below right:{\tiny #4}]{#5};}}

\begin{document}

\tikzset{every node/.style={minimum size=.5cm}}

\begin{center}
\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline
% Line 1
\N{2}{3 4}{5}{}{} & \N{2}{4}{5}{}{} & \N{}{}{}{}{1} &
\N{}{}{}{}{9} & \N{2}{3}{}{}{} & \N{}{}{}{}{7} &
\N{}{}{5 6}{}{} & \N{}{4}{5 6}{}{} & \N{}{}{}{}{8} \\ \hline

% Line 2
\N{}{}{}{}{6} & \N{2}{4}{}{9}{} & \N{2}{}{}{9}{} &
\N{}{}{}{}{1} & \N{}{}{}{}{8} & \N{}{}{}{}{5} &
\N{}{}{}{}{7} & \N{}{}{}{}{3} & \N{2}{4}{}{9}{} \\ \hline

% Line 3
\N{2}{3}{5}{8 9}{} & \N{2}{}{5}{8 9}{} & \N{}{}{}{}{7} &
\N{}{}{}{}{4} & \N{}{}{}{}{6} & \N{2}{3}{}{}{} &
\N{}{}{}{}{1} & \N{}{}{5}{9}{} & \N{2}{}{5}{9}{} \\ \hline\hline

% Line 4
\N{1 2}{}{5}{8}{} & \N{}{}{}{}{3} & \N{}{}{}{}{4} &
\N{2}{}{6}{7}{} & \N{}{}{}{}{9} & \N{2}{}{6}{8}{} &
\N{}{}{5 6}{8}{} & \N{1}{}{5 6}{7 8}{} & \N{1}{}{5 6}{}{} \\ \hline

% Line 5
\N{1 2}{}{}{8 9}{} & \N{2}{}{6}{7 8 9}{} & \N{2}{}{6}{8 9}{} &
\N{}{}{}{}{5} & \N{2}{3}{}{}{} & \N{}{}{}{}{4} &
\N{}{3}{6}{8}{} & \N{1}{}{6}{7 8 9}{} & \N{1}{3}{6}{9}{} \\ \hline

% Line 6
\N{}{}{5}{8 9}{} & \N{}{}{5 6}{7 8 9}{} & \N{}{}{6}{8 9}{} &
\N{}{3}{6}{7}{} & \N{}{}{}{}{1} & \N{}{3}{6}{8}{} &
\N{}{}{}{}{4} & \N{}{}{}{}{2} & \N{}{3}{5 6}{9}{} \\ \hline\hline

% Line 7
\N{2}{3 4}{}{8}{} & \N{2}{4}{6}{8}{} & \N{}{}{}{}{5} &
\N{2}{3}{6}{}{} & \N{}{}{}{}{7} & \N{}{}{}{}{1} &
\N{}{}{}{}{9} & \N{}{4}{6}{8}{} & \N{}{3 4}{6}{}{} \\ \hline

% Line 8
\N{2}{3}{}{9}{} & \N{}{}{}{}{1} & \N{2}{3}{6}{9}{} &
\N{}{}{}{}{8} & \N{}{}{}{}{4} & \N{2}{3}{6}{}{} &
\N{}{3}{5 6}{}{} & \N{}{}{5 6}{}{} & \N{}{}{}{}{7} \\ \hline

% Line 9
\N{}{}{}{}{7} & \N{}{4}{6}{8}{} & \N{}{3}{6}{8}{} &
\N{}{3}{6}{}{} & \N{}{}{}{}{5} & \N{}{}{}{}{9} &
\N{}{}{}{}{2} & \N{1}{4}{6}{8}{} & \N{1}{3 4}{6}{}{} \\ \hline\hline
\end{tabular}
\end{center}

\end{document}

        """
pdf = latex2pdf(document)