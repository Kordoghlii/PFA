/**
 * Calcule la somme de deux nombres.
 *
 * @param {number} a - Le premier nombre.
 * @param {number} b - Le second nombre.
 * @returns {number} La somme de a et b.
 *
 * @example
 * const resultat = addition(3, 4);
 * console.log(resultat); // 7
 */
function addition(a, b) {
    // Vérifie que les entrées sont bien des nombres
    if (typeof a !== 'number' || typeof b !== 'number') {
      throw new Error('Les deux arguments doivent être des nombres.');
    }
  
    return a + b;
  }
  
  /**
   * Vérifie si un mot est un palindrome.
   *
   * @param {string} mot - Le mot à tester.
   * @returns {boolean} True si le mot est un palindrome, false sinon.
   *
   * @example
   * const estValide = estPalindrome("radar");
   * console.log(estValide); // true
   */
  function estPalindrome(mot) {
    // Nettoie la chaîne en supprimant les espaces et en mettant en minuscules
    const nettoye = mot.toLowerCase().replace(/\s+/g, '');
    // Compare la chaîne à son inverse
    return nettoye === nettoye.split('').reverse().join('');
  }
  