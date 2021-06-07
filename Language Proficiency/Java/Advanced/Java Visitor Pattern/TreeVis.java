import java.util.ArrayList;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

import java.util.ArrayList;
import java.util.Scanner;

enum Color {
    RED, GREEN
}

abstract class Tree {
    private int value;
    private Color color;
    private int depth;

    public Tree(int value, Color color, int depth) {
        this.value = value;
        this.color = color;
        this.depth = depth;
    }

    public int getValue() {
        return value;
    }

    public Color getColor() {
        return color;
    }

    public int getDepth() {
        return depth;
    }

    public abstract void accept(TreeVis visitor);
}

class TreeNode extends Tree {
    private ArrayList<Tree> children = new ArrayList<>();

    public TreeNode(int value, Color color, int depth) {
        super(value, color, depth);
    }

    public void accept(TreeVis visitor) {
        visitor.visitNode(this);

        for (Tree child : children) {
            child.accept(visitor);
        }
    }

    public void addChild(Tree child) {
        children.add(child);
    }
}

class TreeLeaf extends Tree {
    public TreeLeaf(int value, Color color, int depth) {
        super(value, color, depth);
    }

    public void accept(TreeVis visitor) {
        visitor.visitLeaf(this);
    }
}

abstract class TreeVis {
    public abstract int getResult();
    public abstract void visitNode(TreeNode node);
    public abstract void visitLeaf(TreeLeaf leaf);
}

class SumInLeavesVisitor extends TreeVis {
	private int result = 0;
    
    public int getResult() {
      	//implement this
        return result;
    }

    public void visitNode(TreeNode node) {
      	//implement this
    }

    public void visitLeaf(TreeLeaf leaf) {
      	//implement this
        result += leaf.getValue();
    }
}

class ProductOfRedNodesVisitor extends TreeVis {
    private long result = 1;
    private final int modulo = 1000000007;
    
    public int getResult() {
      	//implement this
        return (int) result;
    }

    public void visitNode(TreeNode node) {
      	//implement this
        if (node.getColor() == Color.RED) {
            result = (result * node.getValue()) % modulo;
        }
    }

    public void visitLeaf(TreeLeaf leaf) {
      	//implement this
        if (leaf.getColor() == Color.RED) {
            result = (result * leaf.getValue()) % modulo;
        }
    }
}

class FancyVisitor extends TreeVis {
    private int nonLeafEvenDepthSum = 0;
    private int greenLeavesSum = 0;
    
    public int getResult() {
      	//implement this
        return Math.abs(nonLeafEvenDepthSum - greenLeavesSum);
    }

    public void visitNode(TreeNode node) {
    	//implement this
        if (node.getDepth() % 2 == 0) {
            nonLeafEvenDepthSum += node.getValue();
        }
    }

    public void visitLeaf(TreeLeaf leaf) {
    	//implement this
        if (leaf.getColor() == Color.GREEN) {
            greenLeavesSum += leaf.getValue();
        }
    }
}

public class Solution {
    private static int[] values;
    private static Color[] colors;
    private static HashMap<Integer, HashSet<Integer>> neighbors;
  
    public static Tree solve() {
        //read the tree from STDIN and return its root as a return value of this function
        Scanner sc = new Scanner(System.in);
        int numNodes = sc.nextInt();
            
        values = new int[numNodes];
        colors = new Color[numNodes];
        neighbors = new HashMap<>(numNodes);
            
        for (int i = 0; i < numNodes; i++) {
            values[i] = sc.nextInt();
        }
        for (int i = 0; i < numNodes; i++) {
            colors[i] = sc.nextInt() == 0 ? Color.RED : Color.GREEN;
        }
        if (numNodes == 1) {
            return new TreeLeaf(values[0], colors[0], 0);
        }
            
        for (int i = 0; i < numNodes - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
                
            HashSet<Integer> uNeighbors = neighbors.get(u);
            if (uNeighbors == null) {
                uNeighbors = new HashSet<>();
                neighbors.put(u, uNeighbors);
            }
            uNeighbors.add(v);
                
            HashSet<Integer> vNeighbors = neighbors.get(v);
            if (vNeighbors == null) {
                vNeighbors = new HashSet<>();
                neighbors.put(v, vNeighbors);
            }
            vNeighbors.add(u);
        }
            
        sc.close();
            
        TreeNode root = new TreeNode(values[0], colors[0], 0);
        build(root, 1);
        return root;
    }
        
    private static void build(TreeNode parent, int num) {
        for (int child : neighbors.get(num)) {
            neighbors.get(child).remove(num);
                
            HashSet<Integer> grandChildren = neighbors.get(child);
            boolean hasChild = (grandChildren != null && !grandChildren.isEmpty());
            Tree tree;
            if (hasChild) {
                tree = new TreeNode(values[child-1], colors[child-1], parent.getDepth()+1);
            } else {
                tree = new TreeLeaf(values[child-1], colors[child-1], parent.getDepth()+1);
            }
            parent.addChild(tree);
                
            if (tree instanceof TreeNode) {
                build((TreeNode) tree, child);
            }
        }
    }

    public static void main(String[] args) {
      	Tree root = solve();
		SumInLeavesVisitor vis1 = new SumInLeavesVisitor();
      	ProductOfRedNodesVisitor vis2 = new ProductOfRedNodesVisitor();
      	FancyVisitor vis3 = new FancyVisitor();

      	root.accept(vis1);
      	root.accept(vis2);
      	root.accept(vis3);

      	int res1 = vis1.getResult();
      	int res2 = vis2.getResult();
      	int res3 = vis3.getResult();

      	System.out.println(res1);
     	System.out.println(res2);
    	System.out.println(res3);
	}
}

