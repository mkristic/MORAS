Require Import Bool.

Notation " ! b " := (negb b) (at level 0).

(* Zad 1. a *)

Goal forall x y,
  !(x && y) || (!x && y) || (!x && !y) = !(x && y).
Proof.
  intros x y. destruct x, y ; simpl ; reflexivity.
Qed.


(* Zad 2. b *)

Goal forall x y z,
  !(!x && y && !z) && !(x && y && z) && (x && !y && !z)
  = x && !(y || z).
Proof.
  intros x y z. destruct x, y, z ; simpl ; reflexivity.
Qed.