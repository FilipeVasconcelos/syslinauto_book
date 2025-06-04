# Systèmes et automatique linéaires

## Contexte

Ce document est le résultat de l'enseignement dispensé de janvier 2018 
à juin 2022 en deuxième année de l'ESME Sudria. Celui-ci était associé 
au module de Systèmes Mécaniques et Automatiques (SMA).

## PDF (dernière version)
[PDF](sma_auto.pdf)

<<<<<<< HEAD
## Sommaire 

<h2>Table of Contents</h2>
<ul>
<li><a href="#section-1">1 Systèmes linéaires, continus</a><span class="page">p.15</span></li>
  <li><a href="#section-1">1 Introduction</a><span class="page">p.16</span></li>
  <li><a href="#section-2">2 Définition SLCI</a><span class="page">p.17</span></li>
    <li><a href="#section-2.1">2.1 La notion de Système</a><span class="page">p.17</span></li>
    <li><a href="#section-2.2">2.2 Propriétés des SLCI</a><span class="page">p.18</span></li>
  <li><a href="#section-3">3 Modélisation d'un SLCI</a><span class="page">p.19</span></li>
    <li><a href="#section-3.1">3.1 \'Equation différentielle à coefficients constants</a><span class="page">p.19</span></li>
    <li><a href="#section-3.2">3.2 Exemples de mises en équation</a><span class="page">p.20</span></li>
  <li><a href="#section-4">4 Modélisation d'un signal</a><span class="page">p.21</span></li>
    <li><a href="#section-4.1">4.1 Propriétés des signaux continus</a><span class="page">p.21</span></li>
    <li><a href="#section-4.2">4.2 Signaux usuels rencontrés</a><span class="page">p.24</span></li>
<li><a href="#section-4.2.1">4.2.1 en entrée</a><span class="page">p.24</span></li>
<li><a href="#section-4.2.2">4.2.2 en sortie</a><span class="page">p.26</span></li>
    <li><a href="#section-4.3">4.3 Décomposition d'un signal en signaux usuels</a><span class="page">p.28</span></li>
  <li><a href="#section-5">5 La transformée de Laplace</a><span class="page">p.29</span></li>
    <li><a href="#section-5.1">5.1 Définition</a><span class="page">p.29</span></li>
    <li><a href="#section-5.2">5.2 Propriétés</a><span class="page">p.30</span></li>
    <li><a href="#section-5.3">5.3 Transformées des signaux usuels</a><span class="page">p.32</span></li>
    <li><a href="#section-5.4">5.4 Application de la transformée de Laplace</a><span class="page">p.35</span></li>
<li><a href="#section-5.4.1">5.4.1 Méthodologie</a><span class="page">p.35</span></li>
<li><a href="#section-5.4.2">5.4.2 Exemple complet</a><span class="page">p.36</span></li>
  <li><a href="#section-6">6 Fonction de Transfert</a><span class="page">p.39</span></li>
    <li><a href="#section-6.1">6.1 Définition</a><span class="page">p.39</span></li>
    <li><a href="#section-6.2">6.2 Lien entre fonction de transfert et réponse impulsionnelle</a><span class="page">p.39</span></li>
    <li><a href="#section-6.3">6.3 Représentation de la fonction de transfert</a><span class="page">p.40</span></li>
<li><a href="#section-6.3.1">6.3.1 Forme canonique de la fonction de transfert</a><span class="page">p.41</span></li>
<li><a href="#section-6.3.2">6.3.2 Forme factorisée de la fonction de transfert</a><span class="page">p.42</span></li>
<li><a href="#section-6.3.3">6.3.3 Carte des pôles et zéros d'une fonction de transfert</a><span class="page">p.43</span></li>
  <li><a href="#section-7">7 Exercices du chapitre</a><span class="page">p.44</span></li>
  <li><a href="#section-8">8 Corrigé des exercices</a><span class="page">p.48</span></li>
<li><a href="#section-2">2 Schémas fonctionnels</a><span class="page">p.57</span></li>
  <li><a href="#section-1">1 Introduction</a><span class="page">p.58</span></li>
  <li><a href="#section-2">2 \'Eléments de base des schémas fonctionnels</a><span class="page">p.58</span></li>
  <li><a href="#section-3">3 Transformation des schémas fonctionnels</a><span class="page">p.60</span></li>
    <li><a href="#section-3.1">3.1 Réduction de schéma-bloc</a><span class="page">p.60</span></li>
    <li><a href="#section-3.2">3.2 Manipulation de schéma-bloc</a><span class="page">p.62</span></li>
  <li><a href="#section-4">4 Cas d'entrées multiples</a><span class="page">p.64</span></li>
  <li><a href="#section-5">5 Réduction de schéma-bloc de grande taille</a><span class="page">p.65</span></li>
    <li><a href="#section-5.1">5.1 Exemple à entrée simple</a><span class="page">p.65</span></li>
    <li><a href="#section-5.2">5.2 Exemple à entrées multiples</a><span class="page">p.67</span></li>
  <li><a href="#section-6">6 Graphe de fluence</a><span class="page">p.68</span></li>
    <li><a href="#section-6.1">6.1 Définitions</a><span class="page">p.68</span></li>
    <li><a href="#section-6.2">6.2 Algèbre des graphes de fluences</a><span class="page">p.69</span></li>
    <li><a href="#section-6.3">6.3 Règle de Mason</a><span class="page">p.72</span></li>
  <li><a href="#section-7">7 Schéma-bloc dans le domaine temporel</a><span class="page">p.74</span></li>
    <li><a href="#section-7.1">7.1 Opérateur intégral</a><span class="page">p.74</span></li>
    <li><a href="#section-7.2">7.2 Produit d'un signal temporel par un scalaire</a><span class="page">p.75</span></li>
    <li><a href="#section-7.3">7.3 Représentation d'une équation différentielle</a><span class="page">p.75</span></li>
    <li><a href="#section-7.4">7.4 Application au système masse-ressort</a><span class="page">p.76</span></li>
  <li><a href="#section-8">8 Exercices du chapitre</a><span class="page">p.79</span></li>
  <li><a href="#section-9">9 Corrigé des exercices</a><span class="page">p.83</span></li>
<li><a href="#section-3">3 Modélisation des SLCI</a><span class="page">p.91</span></li>
  <li><a href="#section-1">1 Introduction</a><span class="page">p.92</span></li>
  <li><a href="#section-2">2 Système du premier ordre</a><span class="page">p.92</span></li>
    <li><a href="#section-2.1">2.1 Définition d'un système du premier ordre</a><span class="page">p.92</span></li>
    <li><a href="#section-2.2">2.2 Fonction de transfert d'un système du premier ordre</a><span class="page">p.93</span></li>
    <li><a href="#section-2.3">2.3 Pôle de la fonction de transfert du premier ordre</a><span class="page">p.93</span></li>
    <li><a href="#section-2.4">2.4 Réponses temporelles d'un système du premier ordre</a><span class="page">p.93</span></li>
<li><a href="#section-2.4.1">2.4.1 Réponse impulsionnelle</a><span class="page">p.93</span></li>
<li><a href="#section-2.4.2">2.4.2 Réponse indicielle</a><span class="page">p.95</span></li>
<li><a href="#section-2.4.3">2.4.3 Réponse à une rampe</a><span class="page">p.96</span></li>
  <li><a href="#section-3">3 Système du second ordre</a><span class="page">p.97</span></li>
    <li><a href="#section-3.1">3.1 Définition d'un système du second ordre</a><span class="page">p.97</span></li>
    <li><a href="#section-3.2">3.2 Fonction de transfert d'un système du second ordre</a><span class="page">p.97</span></li>
    <li><a href="#section-3.3">3.3 Pôles de la fonction de transfert du second ordre</a><span class="page">p.97</span></li>
    <li><a href="#section-3.4">3.4 Réponses temporelles d'un système du second ordre</a><span class="page">p.98</span></li>
<li><a href="#section-3.4.1">3.4.1 Réponse impulsionnelle</a><span class="page">p.99</span></li>
<li><a href="#section-3.4.2">3.4.2 Réponse indicielle</a><span class="page">p.100</span></li>
<li><a href="#section-3.4.3">3.4.3 Réponse à une rampe</a><span class="page">p.108</span></li>
    <li><a href="#section-3.5">3.5 Cas particulier de l'oscillateur harmonique</a><span class="page">p.111</span></li>
<li><a href="#section-3.5.1">3.5.1 Réponse impulsionnelle</a><span class="page">p.112</span></li>
  <li><a href="#section-4">4 Autres modèles particuliers</a><span class="page">p.112</span></li>
    <li><a href="#section-4.1">4.1 Gain pur</a><span class="page">p.112</span></li>
    <li><a href="#section-4.2">4.2 Intégrateur pur</a><span class="page">p.112</span></li>
    <li><a href="#section-4.3">4.3 Dérivateur pur</a><span class="page">p.113</span></li>
    <li><a href="#section-4.4">4.4 Retard pur</a><span class="page">p.113</span></li>
  <li><a href="#section-5">5 Généralisation des modèles de SLCI</a><span class="page">p.114</span></li>
    <li><a href="#section-5.1">5.1 Systèmes d'ordre supérieur à 2</a><span class="page">p.114</span></li>
    <li><a href="#section-5.2">5.2 Exemple d'une fonction de transfert d'ordre 3</a><span class="page">p.115</span></li>
  <li><a href="#section-6">6 Identification d'un modèle de comportement</a><span class="page">p.115</span></li>
    <li><a href="#section-6.1">6.1 Formule de Bureau</a><span class="page">p.115</span></li>
    <li><a href="#section-6.2">6.2 Modèle de Strejc</a><span class="page">p.116</span></li>
    <li><a href="#section-6.3">6.3 Modèle de Broïda</a><span class="page">p.116</span></li>
  <li><a href="#section-7">7 Exercices du chapitre</a><span class="page">p.117</span></li>
  <li><a href="#section-8">8 Corrigé des exercices</a><span class="page">p.120</span></li>
<li><a href="#section-4">4 Analyse fréquentielle</a><span class="page">p.127</span></li>
  <li><a href="#section-1">1 Introduction</a><span class="page">p.128</span></li>
  <li><a href="#section-2">2 Réponse harmonique</a><span class="page">p.128</span></li>
    <li><a href="#section-2.1">2.1 Réponse harmonique dans le domaine temporel</a><span class="page">p.130</span></li>
  <li><a href="#section-3">3 Représentation graphique</a><span class="page">p.131</span></li>
    <li><a href="#section-3.1">3.1 Diagramme de Bode</a><span class="page">p.131</span></li>
    <li><a href="#section-3.2">3.2 Diagramme de Nyquist</a><span class="page">p.132</span></li>
    <li><a href="#section-3.3">3.3 Diagramme de Black-Nichols</a><span class="page">p.133</span></li>
  <li><a href="#section-4">4 Analyse fréquentielle des modèles usuels</a><span class="page">p.134</span></li>
    <li><a href="#section-4.1">4.1 Diagrammes de Bode</a><span class="page">p.134</span></li>
<li><a href="#section-4.1.1">4.1.1 Méthodologie générale</a><span class="page">p.134</span></li>
<li><a href="#section-4.1.2">4.1.2 Diagramme de Bode d'un gain pur</a><span class="page">p.135</span></li>
<li><a href="#section-4.1.3">4.1.3 Diagramme de Bode d'un intégrateur pur</a><span class="page">p.136</span></li>
<li><a href="#section-4.1.4">4.1.4 Diagramme de Bode d'un dérivateur pur</a><span class="page">p.137</span></li>
<li><a href="#section-4.1.5">4.1.5 Diagramme de Bode d'un système à retard pur</a><span class="page">p.138</span></li>
<li><a href="#section-4.1.6">4.1.6 Diagramme de Bode d'un système du premier ordre</a><span class="page">p.139</span></li>
<li><a href="#section-4.1.7">4.1.7 Diagramme de Bode de deux systèmes du premier ordre en série</a><span class="page">p.142</span></li>
<li><a href="#section-4.1.8">4.1.8 Diagramme de Bode d'un système second d'ordre</a><span class="page">p.143</span></li>
<li><a href="#section-4.1.9">4.1.9 Diagramme de Bode d'un système d'ordre quelconque</a><span class="page">p.147</span></li>
    <li><a href="#section-4.2">4.2 Diagrammes de Nyquist</a><span class="page">p.150</span></li>
<li><a href="#section-4.2.1">4.2.1 Méthodologie générale</a><span class="page">p.150</span></li>
<li><a href="#section-4.2.2">4.2.2 Diagramme de Nyquist d'un gain pur</a><span class="page">p.150</span></li>
<li><a href="#section-4.2.3">4.2.3 Diagramme de Nyquist d'un intégrateur pur</a><span class="page">p.150</span></li>
<li><a href="#section-4.2.4">4.2.4 Diagramme de Nyquist d'un dérivateur pur</a><span class="page">p.151</span></li>
<li><a href="#section-4.2.5">4.2.5 Diagramme de Nyquist d'un retard pur</a><span class="page">p.151</span></li>
<li><a href="#section-4.2.6">4.2.6 Diagramme de Nyquist d'un système du premier ordre</a><span class="page">p.151</span></li>
<li><a href="#section-4.2.7">4.2.7 Diagramme de Nyquist d'un système du second ordre</a><span class="page">p.153</span></li>
<li><a href="#section-4.2.8">4.2.8 Effet d'un retard sur le diagramme de Nyquist</a><span class="page">p.154</span></li>
    <li><a href="#section-4.3">4.3 Diagrammes de Black-Nichols</a><span class="page">p.155</span></li>
<li><a href="#section-4.3.1">4.3.1 Méthodologie générale</a><span class="page">p.155</span></li>
<li><a href="#section-4.3.2">4.3.2 Diagrammes de Black d'un intégrateur pur</a><span class="page">p.155</span></li>
<li><a href="#section-4.3.3">4.3.3 Diagrammes de Black d'un dérivateur pur</a><span class="page">p.155</span></li>
<li><a href="#section-4.3.4">4.3.4 Diagrammes de Black d'un premier ordre</a><span class="page">p.156</span></li>
<li><a href="#section-4.3.5">4.3.5 Diagrammes de Black d'un second ordre</a><span class="page">p.156</span></li>
  <li><a href="#section-5">5 Etude du transitoire de la réponse harmonique</a><span class="page">p.156</span></li>
    <li><a href="#section-5.1">5.1 Exemple d'un système du premier ordre</a><span class="page">p.157</span></li>
  <li><a href="#section-6">6 Exercices du chapitre</a><span class="page">p.159</span></li>
  <li><a href="#section-7">7 Corrigé des exercices</a><span class="page">p.161</span></li>
<li><a href="#section-5">5 Asservissement Linéaire</a><span class="page">p.169</span></li>
  <li><a href="#section-1">1 Asservissement et régulation</a><span class="page">p.170</span></li>
  <li><a href="#section-2">2 Organisation d'un asservissement</a><span class="page">p.171</span></li>
    <li><a href="#section-2.1">2.1 Schémas fonctionnels associés aux systèmes asservis</a><span class="page">p.171</span></li>
    <li><a href="#section-2.2">2.2 Présence d'une perturbation : la régulation</a><span class="page">p.172</span></li>
    <li><a href="#section-2.3">2.3 Schéma fonctionnel complet</a><span class="page">p.172</span></li>
    <li><a href="#section-2.4">2.4 Fonctions de transfert associées à l'asservissement</a><span class="page">p.173</span></li>
  <li><a href="#section-3">3 Asservissement des SLCI modèles</a><span class="page">p.175</span></li>
    <li><a href="#section-3.1">3.1 Asservissement d'un intégrateur</a><span class="page">p.175</span></li>
    <li><a href="#section-3.2">3.2 Asservissement d'un système du premier ordre</a><span class="page">p.176</span></li>
    <li><a href="#section-3.3">3.3 Asservissement d'un système du second ordre</a><span class="page">p.176</span></li>
  <li><a href="#section-4">4 Exercices du chapitre</a><span class="page">p.178</span></li>
  <li><a href="#section-5">5 Corrigé des exercices</a><span class="page">p.180</span></li>
<li><a href="#section-6">6 Performances des systèmes</a><span class="page">p.183</span></li>
  <li><a href="#section-1">1 Introduction</a><span class="page">p.184</span></li>
  <li><a href="#section-2">2 Précision</a><span class="page">p.184</span></li>
    <li><a href="#section-2.1">2.1 Précision en boucle ouverte</a><span class="page">p.184</span></li>
<li><a href="#section-2.1.1">2.1.1 Exemple d'un premier ordre</a><span class="page">p.185</span></li>
    <li><a href="#section-2.2">2.2 Précision en boucle fermée</a><span class="page">p.185</span></li>
<li><a href="#section-2.2.1">2.2.1 Erreur statique indicielle</a><span class="page">p.186</span></li>
<li><a href="#section-2.2.2">2.2.2 Erreur statique de poursuite</a><span class="page">p.186</span></li>
<li><a href="#section-2.2.3">2.2.3 Erreur statique d'accélération</a><span class="page">p.187</span></li>
    <li><a href="#section-2.3">2.3 Effet d'une perturbation</a><span class="page">p.187</span></li>
<li><a href="#section-2.3.1">2.3.1 Cas générale</a><span class="page">p.187</span></li>
<li><a href="#section-2.3.2">2.3.2 Exemple de rejet de perturbation</a><span class="page">p.189</span></li>
  <li><a href="#section-3">3 Rapidité</a><span class="page">p.192</span></li>
    <li><a href="#section-3.1">3.1 Réponse temporelle</a><span class="page">p.192</span></li>
<li><a href="#section-3.1.1">3.1.1 Temps de réponse à 5\% et temps de montée</a><span class="page">p.192</span></li>
<li><a href="#section-3.1.2">3.1.2 Système du premier ordre</a><span class="page">p.193</span></li>
<li><a href="#section-3.1.3">3.1.3 Système du second ordre</a><span class="page">p.194</span></li>
    <li><a href="#section-3.2">3.2 \'Etude de la rapidité à partir de la réponse harmonique</a><span class="page">p.197</span></li>
    <li><a href="#section-3.3">3.3 Influence des pôles dominants</a><span class="page">p.197</span></li>
  <li><a href="#section-4">4 Exercices du chapitre</a><span class="page">p.199</span></li>
  <li><a href="#section-5">5 Corrigé des exercices</a><span class="page">p.200</span></li>
<li><a href="#section-7">7 Stabilité des systèmes asservis</a><span class="page">p.205</span></li>
  <li><a href="#section-1">1 Contexte et définition de la stabilité</a><span class="page">p.206</span></li>
  <li><a href="#section-2">2 Instabilité de l'asservissement</a><span class="page">p.208</span></li>
  <li><a href="#section-3">3 Condition fondamentale de stabilité</a><span class="page">p.209</span></li>
  <li><a href="#section-4">4 Critère algébrique de Routh-Hurwitz</a><span class="page">p.212</span></li>
    <li><a href="#section-4.1">4.1 Tableau de Routh</a><span class="page">p.212</span></li>
    <li><a href="#section-4.2">4.2 Exemple d'application du critère de Routh-Hurwitz</a><span class="page">p.215</span></li>
  <li><a href="#section-5">5 Critère de stabilité du revers</a><span class="page">p.216</span></li>
    <li><a href="#section-5.1">5.1 Critère de stabilité à partir de la boucle ouverte</a><span class="page">p.216</span></li>
    <li><a href="#section-5.2">5.2 Mise en évidence de l'instabilité en boucle fermée</a><span class="page">p.217</span></li>
    <li><a href="#section-5.3">5.3 Critère du revers dans le plan de Nyquist</a><span class="page">p.219</span></li>
    <li><a href="#section-5.4">5.4 Critère du revers dans le plan de Black</a><span class="page">p.220</span></li>
    <li><a href="#section-5.5">5.5 Critère du revers dans le plan de Bode</a><span class="page">p.220</span></li>
  <li><a href="#section-6">6 Marge de stabilité et robustesse de la stabilité</a><span class="page">p.221</span></li>
    <li><a href="#section-6.1">6.1 Marges de stabilité à partir du diagramme de Nyquist</a><span class="page">p.222</span></li>
    <li><a href="#section-6.2">6.2 Marges de stabilité à partir du diagramme de Bode</a><span class="page">p.222</span></li>
    <li><a href="#section-6.3">6.3 Marges de stabilité à partir du diagramme de Black</a><span class="page">p.222</span></li>
  <li><a href="#section-7">7 Critère de Nyquist</a><span class="page">p.224</span></li>
    <li><a href="#section-7.1">7.1 Image d'un contour par une fonction de transfert</a><span class="page">p.224</span></li>
    <li><a href="#section-7.2">7.2 Principe de l'argument de Cauchy</a><span class="page">p.225</span></li>
    <li><a href="#section-7.3">7.3 Contours de Nyquist et de Bromwich</a><span class="page">p.225</span></li>
    <li><a href="#section-7.4">7.4 \'Enoncé et application du critère de Nyquist</a><span class="page">p.228</span></li>
  <li><a href="#section-8">8 Exercices du chapitre</a><span class="page">p.230</span></li>
  <li><a href="#section-9">9 Corrigé des exercices</a><span class="page">p.232</span></li>
<li><a href="#section-8">8 Correction des systèmes asservis</a><span class="page">p.239</span></li>
  <li><a href="#section-1">1 Nécessité de la correction</a><span class="page">p.240</span></li>
  <li><a href="#section-2">2 Structure de la correction</a><span class="page">p.241</span></li>
  <li><a href="#section-3">3 Correcteurs élémentaires P, I et D</a><span class="page">p.243</span></li>
    <li><a href="#section-3.1">3.1 Correcteur P</a><span class="page">p.243</span></li>
    <li><a href="#section-3.2">3.2 Correcteur I</a><span class="page">p.243</span></li>
    <li><a href="#section-3.3">3.3 Correcteur D</a><span class="page">p.243</span></li>
  <li><a href="#section-4">4 Correcteurs composés</a><span class="page">p.243</span></li>
    <li><a href="#section-4.1">4.1 Correcteur PI</a><span class="page">p.243</span></li>
    <li><a href="#section-4.2">4.2 Correcteur PD</a><span class="page">p.245</span></li>
  <li><a href="#section-5">5 Correcteurs à avance et retard de phase</a><span class="page">p.246</span></li>
    <li><a href="#section-5.1">5.1 Correcteur à avance de phase</a><span class="page">p.246</span></li>
    <li><a href="#section-5.2">5.2 Correcteur à retard de phase</a><span class="page">p.249</span></li>
  <li><a href="#section-6">6 Correcteur PID</a><span class="page">p.251</span></li>
    <li><a href="#section-6.1">6.1 PID idéal</a><span class="page">p.251</span></li>
    <li><a href="#section-6.2">6.2 PID amélioré</a><span class="page">p.253</span></li>
  <li><a href="#section-7">7 Exercices du chapitre</a><span class="page">p.255</span></li>
  <li><a href="#section-8">8 Corrigé des exercices</a><span class="page">p.258</span></li>
<li><a href="#section-9">9 Représentation d'état</a><span class="page">p.269</span></li>
  <li><a href="#section-1">1 Contexte</a><span class="page">p.270</span></li>
    <li><a href="#section-1.1">1.1 Système multivariable</a><span class="page">p.270</span></li>
  <li><a href="#section-2">2 \'Etat d'un système dynamique</a><span class="page">p.272</span></li>
    <li><a href="#section-2.1">2.1 \'Equation d'état et équation de sortie</a><span class="page">p.272</span></li>
    <li><a href="#section-2.2">2.2 Intégration de l'équation d'état</a><span class="page">p.273</span></li>
    <li><a href="#section-2.3">2.3 Représentation en schéma bloc</a><span class="page">p.273</span></li>
    <li><a href="#section-2.4">2.4 Lien entre la fonction de transfert et la réprésentation d'état</a><span class="page">p.273</span></li>
  <li><a href="#section-3">3 Application de la représentation d'état</a><span class="page">p.275</span></li>
    <li><a href="#section-3.1">3.1 Représentation d'état du système</a><span class="page">p.275</span></li>
    <li><a href="#section-3.2">3.2 Passage de la représentation d'état à la fonction de transfert</a><span class="page">p.276</span></li>
  <li><a href="#section-4">4 Exercices du chapitre</a><span class="page">p.278</span></li>
  <li><a href="#section-5">5 Corrigé des exercices</a><span class="page">p.279</span></li>
<li><a href="#section-A">A Alphabet Grec</a><span class="page">p.283</span></li>
<li><a href="#section-B">B Unités du Système International</a><span class="page">p.285</span></li>
<li><a href="#section-C">C Pierre-Simon de Laplace</a><span class="page">p.287</span></li>
<li><a href="#section-D">D Transformation de Laplace</a><span class="page">p.289</span></li>
  <li><a href="#section-1">1 Définition</a><span class="page">p.289</span></li>
  <li><a href="#section-2">2 Propriétés</a><span class="page">p.289</span></li>
  <li><a href="#section-3">3 Table des transformées de Laplace</a><span class="page">p.291</span></li>
<li><a href="#section-E">E Les nombres complexes</a><span class="page">p.293</span></li>
<li><a href="#section-F">F Analyse de Fourier</a><span class="page">p.297</span></li>
  <li><a href="#section-1">1 Série de Fourier</a><span class="page">p.297</span></li>
<li><a href="#section-G">G Équations différentielles à coefficients constants</a><span class="page">p.299</span></li>
  <li><a href="#section-1">1 Premier ordre</a><span class="page">p.299</span></li>
    <li><a href="#section-1.1">1.1 Forme canonique</a><span class="page">p.299</span></li>
    <li><a href="#section-1.2">1.2 Sans second membre</a><span class="page">p.299</span></li>
    <li><a href="#section-1.3">1.3 Avec second membre</a><span class="page">p.300</span></li>
  <li><a href="#section-2">2 Second ordre</a><span class="page">p.301</span></li>
<li><a href="#section-H">H Décomposition en éléments simples</a><span class="page">p.303</span></li>
  <li><a href="#section-1">1 Contexte</a><span class="page">p.303</span></li>
  <li><a href="#section-2">2 Fractions rationnelles rencontrées en automatique</a><span class="page">p.303</span></li>
  <li><a href="#section-3">3 Décomposition en éléments simples</a><span class="page">p.303</span></li>
  <li><a href="#section-4">4 Détermination des coefficients de la DES</a><span class="page">p.304</span></li>
    <li><a href="#section-4.1">4.1 Par identification</a><span class="page">p.304</span></li>
<li><a href="#section-I">I Systèmes du second ordre</a><span class="page">p.307</span></li>
  <li><a href="#section-1">1 Abaques de la réponse temporelle</a><span class="page">p.308</span></li>
  <li><a href="#section-2">2 Analyse fréquentielle</a><span class="page">p.310</span></li>
<li><a href="#section-J">J Initiation à Scilab</a><span class="page">p.311</span></li>
  <li><a href="#section-1">1 Présentation générale</a><span class="page">p.311</span></li>
  <li><a href="#section-2">2 Syntaxe : console</a><span class="page">p.311</span></li>
  <li><a href="#section-3">3 Polynômes et fractions rationnelles</a><span class="page">p.311</span></li>
  <li><a href="#section-4">4 Vecteurs et matrices</a><span class="page">p.313</span></li>
  <li><a href="#section-5">5 Programmation</a><span class="page">p.314</span></li>
  <li><a href="#section-6">6 Tracer de figures</a><span class="page">p.315</span></li>
    <li><a href="#section-7.1">7.1 Définition d'un système linéaire</a><span class="page">p.316</span></li>
    <li><a href="#section-7.2">7.2 Simulation temporelle d'un système linéaire</a><span class="page">p.317</span></li>
    <li><a href="#section-7.3">7.3 Carte des pôles et zéros</a><span class="page">p.318</span></li>
    <li><a href="#section-7.4">7.4 Asservissement</a><span class="page">p.320</span></li>
  <li><a href="#section-8">8 Scilab-Xcos</a><span class="page">p.321</span></li>
    <li><a href="#section-8.1">8.1 Lancer Xcos</a><span class="page">p.321</span></li>
    <li><a href="#section-8.2">8.2 Diagramme simple</a><span class="page">p.321</span></li>
    <li><a href="#section-8.3">8.3 Simulation</a><span class="page">p.321</span></li>
    <li><a href="#section-8.4">8.4 Blocs \@FB@og To Workspace \@FB@fg ~ou \@FB@og From Workspace\@FB@fg </a><span class="page">p.322</span></li>
  <li><a href="#section-9">9 Exemple complet</a><span class="page">p.323</span></li>
<li><a href="#section-K">K Initiation à MATLAB</a><span class="page">p.325</span></li>
  <li><a href="#section-1">1 Présentation générale</a><span class="page">p.326</span></li>
  <li><a href="#section-2">2 Présentation de l'environnemental MATLAB</a><span class="page">p.326</span></li>
  <li><a href="#section-3">3 Génération de signaux usuels</a><span class="page">p.328</span></li>
    <li><a href="#section-3.1">3.1 Vecteur temps</a><span class="page">p.328</span></li>
    <li><a href="#section-3.2">3.2 Génération d'un échelon</a><span class="page">p.328</span></li>
    <li><a href="#section-3.3">3.3 Génération d'une rampe</a><span class="page">p.328</span></li>
    <li><a href="#section-3.4">3.4 Génération d'une impulsion de Dirac</a><span class="page">p.329</span></li>
  <li><a href="#section-4">4 Systèmes linéaires, continus et invariants</a><span class="page">p.329</span></li>
    <li><a href="#section-4.1">4.1 Représentation des polynômes avec MATLAB</a><span class="page">p.329</span></li>
    <li><a href="#section-4.2">4.2 Représentation d'une fonction de transfert</a><span class="page">p.330</span></li>
    <li><a href="#section-4.3">4.3 Réponses temporelles</a><span class="page">p.330</span></li>
<li><a href="#section-4.3.1">4.3.1 Fonctions prédéfinies</a><span class="page">p.330</span></li>
<li><a href="#section-4.3.2">4.3.2 Calcul de la réponse à une entrée quelconque</a><span class="page">p.330</span></li>
  <li><a href="#section-5">5 Exemple d'application</a><span class="page">p.332</span></li>
<li><a href="#section-L">L \'Echelle logarithmique et le décibel~</a><span class="page">p.333</span></li>
  <li><a href="#section-1">1 Rappel sur le logarithme décimal</a><span class="page">p.333</span></li>
  <li><a href="#section-2">2 \'Echelle logarithmique décimale</a><span class="page">p.333</span></li>
  <li><a href="#section-3">3 Le décibel</a><span class="page">p.334</span></li>
  <li><a href="#section-4">4 Diagramme de Bode</a><span class="page">p.335</span></li>
    <li><a href="#section-4.1">4.1 Tracé d'un diagramme de Bode avec MATLAB</a><span class="page">p.336</span></li>
<li><a href="#section-M">M Transformée de Laplace inverse~</a><span class="page">p.337</span></li>
  <li><a href="#section-1">1 Contexte</a><span class="page">p.337</span></li>
  <li><a href="#section-2">2 Algorithme de Gaver-Stehfest</a><span class="page">p.337</span></li>
  <li><a href="#section-3">3 Algorithme fixe de Talbot</a><span class="page">p.340</span></li>
  <li><a href="#section-4">4 Applications aux SLCI</a><span class="page">p.341</span></li>
<li><a href="#section-N">N Abaque de Black-Nichols~</a><span class="page">p.343</span></li>
  <li><a href="#section-1">1 Contexte</a><span class="page">p.343</span></li>
    <li><a href="#section-2.1">2.1 M-cercles</a><span class="page">p.343</span></li>
    <li><a href="#section-2.2">2.2 N-cercles</a><span class="page">p.343</span></li>
  <li><a href="#section-3">3 Abaque de Black-Nichols</a><span class="page">p.345</span></li>
  <li><a href="#section-4">4 Exemples d'application</a><span class="page">p.346</span></li>
<li><a href="#section-O">O Principe de l'argument de Cauchy~</a><span class="page">p.349</span></li>
  <li><a href="#section-2">2 Contour dans le plan complexe</a><span class="page">p.350</span></li>
  <li><a href="#section-3">3 Image d'un contour par une fonction de transfert</a><span class="page">p.351</span></li>
    <li><a href="#section-3.1">3.1 Fonction de transfert avec un seul zéro</a><span class="page">p.351</span></li>
<li><a href="#section-3.1.1">3.1.1 Contour ne contenant pas le zéro parcouru</a><span class="page">p.351</span></li>
<li><a href="#section-3.1.2">3.1.2 Contour contenant le zéro</a><span class="page">p.352</span></li>
    <li><a href="#section-3.2">3.2 Fonction de transfert possédant un pôle</a><span class="page">p.353</span></li>
<li><a href="#section-3.2.1">3.2.1 Contour ne contenant pas le pôle</a><span class="page">p.353</span></li>
<li><a href="#section-3.2.2">3.2.2 Contour contenant le pôle</a><span class="page">p.354</span></li>
  <li><a href="#section-4">4 Enoncé du principe de l'argument de Cauchy</a><span class="page">p.355</span></li>
<li><a href="#section-P">P Lieu d'Evans (lieu des racines)</a><span class="page">p.357</span></li>
  <li><a href="#section-1">1 Régles de construction</a><span class="page">p.357</span></li>
</ul>


=======
>>>>>>> e8756487409d6a4b7e0a1e372758db14a9424ef7
## Page de couverture (Illustration : Lorraine Bayard)
<img src="fig/cover/premiere_page.png" width="256"> <img src="fig/cover/quatrieme_page.png" width="256">

## Auteur
Filipe Manuel Vasconcelos (Enseignant à ESME Lille)
