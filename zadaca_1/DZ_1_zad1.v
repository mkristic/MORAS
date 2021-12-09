Require Import Bool.

Notation " ! b " := (negb b) (at level 0).

(* Zad. 1. a) *)

Goal forall x y,
  !(x && y) || (!x && y) || (!x && !y) = !(x && y).
Proof.
  destruct x, y ; reflexivity.
Qed.


(* Zad. 1. b) *)

Goal forall x y z,
  !(!x && y && !z) && !(x && y && z) && (x && !y && !z) = x && !(y || z).
Proof.
  destruct x, y, z ; reflexivity.
Qed.