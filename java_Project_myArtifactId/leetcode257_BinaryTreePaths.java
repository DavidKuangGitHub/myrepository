/*leetcode257_BinaryTreePaths.java
 * Given a binary tree, return all root-to-leaf paths. Note: A leaf is a node with no children.
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
}
*/
import java.util.ArrayList;
import java.util.List;

public class leetcode257_BinaryTreePaths {
	private List<String> result = new ArrayList<>();

	public List<String> binaryTreePaths(TreeNode root) {
		constructPath(root, new StringBuilder());
		return result;
	}
	
	static TreeNode root;

	private void constructPath(TreeNode node, StringBuilder path) {
		if (node == null)
			return;
		path.append(node.val);
		if (node.left == null && node.right == null) {
			result.add(path.toString());
		} else {
			path.append("->");
			int len = path.length();
			constructPath(node.left, path);
			path.setLength(len); // back track
			constructPath(node.right, path);
			path.setLength(len); // back track
		}
	}
	
	public static void main(String[] args) { 
		leetcode257_BinaryTreePaths mylc_BTP = new leetcode257_BinaryTreePaths();
		mylc_BTP.root = new TreeNode(1);
		mylc_BTP.root.left = new TreeNode(2);
		mylc_BTP.root.right = new TreeNode(3);
		mylc_BTP.root.left.right = new TreeNode(5);
		List<String> paths = mylc_BTP.binaryTreePaths(root);
		for(String path: paths) {
			System.out.println(path);
		}		
	}
}