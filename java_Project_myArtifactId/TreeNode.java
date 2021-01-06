import java.util.ArrayList;
import java.util.List;

public class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode() {
	}

	TreeNode(int val) {
		this.val = val;
	}

	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
	
	/*public List<List<String>> printTree(TreeNode root) {
        List<List<String>> res = new ArrayList<>();
        int height = getHeight(root);
        int length = (int)Math.pow(2, height) - 1;
        for (int i = 0; i < height; i++) {
            res.add(new ArrayList<>());
            for (int j = 0; j < length; j++) {
                res.get(i).add("");
            }
        }
        helper(root, res, 0, 0, length-1);
        return res;
    }
    
    void helper(TreeNode node, List<List<String>> res, int layer, int left, int right) {
        int index = left + (right - left) / 2;
        res.get(layer).set(index, "" + node.val);
        if (node.left != null) {
            helper(node.left, res, layer+1, left, index-1);
        }
        if (node.right != null) {
            helper(node.right, res, layer+1, index+1, right);
        }
        
    }
    
    int getHeight(TreeNode node) {
        if (node == null) {
            return 0;
        }
        return 1 + Math.max(getHeight(node.left), getHeight(node.right));
    }*/
}